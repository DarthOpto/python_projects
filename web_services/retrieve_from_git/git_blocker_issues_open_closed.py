import requests
import git_calls as gc
import datetime
from operator import itemgetter


def issues_from_git():
    issues = []
    count = 1
    while True:
        request = requests.get(gc.CLOSED_BLOCKER_BUGS.format(count), auth=(gc.USERNAME, gc.PASSWORD))
        parsed_response = request.json()
        if not parsed_response:
            break
        for items in parsed_response:
            issue_id = items.get('number')
            date_created = items.get('created_at')[:10]
            date_closed = items.get('closed_at')[:10]
            d1 = datetime.datetime.strptime(date_created, '%Y-%m-%d')
            d2 = datetime.datetime.strptime(date_closed, '%Y-%m-%d')
            closed_time = abs((d2 - d1).days)

            # days_to_close = date_created - date_closed
            issues.append({'create_date': date_created,
                           'closed_date': date_closed,
                           'time_to_close': closed_time,
                           'Issue_ID': issue_id})
        count += 1
    sorted_issues = sorted(issues, key=itemgetter('closed_date'), reverse=True)
    return sorted_issues


def rolling_average():
    closed_days = []
    first_six = issues_from_git()[:6]
    for item in first_six:
        number_of_days = item.get('time_to_close')
        closed_days.append(number_of_days)

    sum_of_days = sum(closed_days)
    average = sum_of_days / len(closed_days)
    return average

