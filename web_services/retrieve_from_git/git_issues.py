import requests
import web_services.retrieve_from_git.git_calls as gc

ISSUE_CALLS = {'blocker': gc.BLOCKER_ISSUES,
               'high': gc.HIGH_ISSUES,
               'normal': gc.NORMAL_ISSUES,
               'low': gc.LOW_ISSUES,
               'customer reported': gc.CUSTOMER_REPORTED_ISSUES
               }


def issue_counts():
    results = []
    issues = []

    for key, value in ISSUE_CALLS.items():
        request = requests.get(value, auth=(gc.USERNAME, gc.PASSWORD))
        parsed_response = request.json()
        number_of_issues = parsed_response.get('total_count')
        issue = parsed_response.get('items')
        issues.append((issue[1].get('number'), issue[1].get('created_at')))
        results.append((key, number_of_issues, issues))
    return results


print(issue_counts())
