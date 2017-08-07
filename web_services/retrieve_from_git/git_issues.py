import requests
import web_services.retrieve_from_git.git_calls as gc


ISSUE_CALLS = {'blocker': gc.BLOCKER_ISSUES,
               'high': gc.HIGH_ISSUES,
               'normal': gc.NORMAL_ISSUES,
               'low': gc.LOW_ISSUES,
               # TODO - Uncomment when we have Customer Reported Issues
               # 'customer reported': gc.CUSTOMER_REPORTED_ISSUES
               }


def issue_counts():
    issues = []

    for priority_key, priority_value in ISSUE_CALLS.items():
        request = requests.get(priority_value, auth=(gc.USERNAME, gc.PASSWORD))
        parsed_response = request.json()
        issue = parsed_response.get('items')
        for items in issue:
            year_month = items.get('created_at')[:7]
            issues.append({'issue_priority': priority_key,
                           'year_month': year_month,
                           'issue_number': issue[1].get('number')})

    return issues


def sort_by_year_month():
    result = {}
    for issue in issue_counts():
        priority = issue['issue_priority']
        month = result.setdefault(issue['year_month'], {})
        month[priority] = month.get(priority, 0) + 1

    return result

print(sort_by_year_month())

