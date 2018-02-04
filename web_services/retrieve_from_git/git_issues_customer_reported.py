import requests
import web_services.retrieve_from_git.git_calls as gc
import datetime


def issues_from_git():
    issues = []
    count = 1
    while True:
        request = requests.get(gc.CUSTOMER_REPORTED.format(count), auth=(gc.USERNAME, gc.PASSWORD))

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




