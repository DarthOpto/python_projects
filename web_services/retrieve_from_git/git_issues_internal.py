import requests
import web_services.retrieve_from_git.git_calls as gc
import csv

# TODO - ADD Customer Reported, once we get some.


def issues_from_git():
    issues = []
    count = 1
    while True:
        request = requests.get(gc.OPEN_ISSUES.format(count), auth=(gc.USERNAME, gc.PASSWORD))

        parsed_response = request.json()
        if not parsed_response:
            break
        for items in parsed_response:
            year_month = items.get('created_at')[:7]
            state = items.get('state')
            issues.append({'year_month': year_month,
                           'state': state})
        count += 1
    return issues


def sort_by_year_month():
    result = {}
    for issue in issues_from_git():
        if issue['year_month'] not in result:
            result[issue['year_month']] = {'open': 0, 'closed': 0}
        if issue['state'] == 'open':
            result[issue['year_month']]['open'] += 1
        if issue['state'] == 'closed':
            result[issue['year_month']]['closed'] += 1

    return result


def send_to_csv():
    data = sort_by_year_month()
    with open('Issues_by_Month_Not_Customer_Reported.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow(['Month',
                              'Opened Issues',
                              'Closed Issues',
                              ])
        for date in data:
            row = [date]
            for key, value in data[date].items():
                row.append(value)
            file_writer.writerow(row)

send_to_csv()



