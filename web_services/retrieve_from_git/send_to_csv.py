import csv
import datetime
import requests
import sys
import git_calls as gc
import git_blocker_issues_open_closed as blockers_rolling_avg


def issues_from_git(issue_type):
    issues = []
    count = 1
    while True:
        request = requests.get(issue_type.format(count), auth=(gc.USERNAME, gc.PASSWORD))
        parsed_response = request.json()
        if not parsed_response:
            break
        for items in parsed_response:
            last_month = str(datetime.datetime.now() + datetime.timedelta(-30))[:7]
            year_month = items.get('created_at')[:7]
            if year_month == last_month:
                state = items.get('state')
                issues.append({'year_month': year_month,
                               'state': state})
        count += 1
    return issues


def sort_by_year_month(issues):
    result = {}
    for issue in issues:
        if issue['year_month'] not in result:
            result[issue['year_month']] = {'open': 0, 'closed': 0}
        if issue['state'] == 'open':
            result[issue['year_month']]['open'] += 1
        if issue['state'] == 'closed':
            result[issue['year_month']]['closed'] += 1

    return result


def send_to_csv():
    internal_data = sort_by_year_month(issues_from_git(gc.OPEN_ISSUES))
    customer_data = sort_by_year_month(issues_from_git(gc.CUSTOMER_REPORTED))
    blocker_data = sort_by_year_month(issues_from_git(gc.BLOCKER_BUGS))
    avg = blockers_rolling_avg.rolling_average()

    with open('Integrated.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow(['Month',
                              'Blockers Rolling Avg',
                              'Opened Issues',
                              'Closed Issues',
                              'Customer Reported Issue Opened',
                              'Customer Reported Issue Closed',
                              'Blocker Bugs Opened',
                              'Blocker Bugs Closed'
                              ])
        row = []
        for date in internal_data:
            row = [date, avg]
            for internal_value in internal_data[date].values():
                row.append(internal_value)
            for customer_issue in customer_data:
                for customer_value in customer_data[customer_issue].values():
                    row.append(customer_value)
            for blocker_issue in blocker_data:
                for blocker_value in blocker_data[blocker_issue].values():
                    row.append(blocker_value)
        file_writer.writerow(row)


if __name__ == '__main__':
    sys.exit(send_to_csv())

