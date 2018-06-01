import requests
import git_calls as gc
import csv
import sys


def issues_from_git():
    issues = []
    count = 1
    while True:
        request = requests.get(gc.OPEN_ISSUES.format(count), auth=(gc.USERNAME, gc.PASSWORD))
        parsed_response = request.json()
        if not parsed_response:
            break
        for items in parsed_response:
            issue_id = items.get('number')
            date_created = items.get('created_at')[:10]
            title = items.get('title')
            url = items.get('html_url')
            label = []
            for labels in items.get('labels'):
                label_name = labels.get('name')
                label.append(label_name)

            # days_to_close = date_created - date_closed
            issues.append({
                'Issue_ID': issue_id,
                'create_date': date_created,
                'title': title,
                'labels': label,
                'URL': url,
            })
        count += 1
    # sorted_issues = sorted(issues, key=itemgetter('closed_date'), reverse=True)
    #     # return sorted_issues
    return issues


def send_to_csv():
    existing_issues = issues_from_git()

    with open('ExistingIssues.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow(['Issue ID',
                              'Create Date',
                              'Title',
                              'Labels',
                              'URL',
                              ])

        for item in existing_issues:
            ID = item.get('Issue_ID')
            create_date = item.get('create_date')
            title = item.get('title')
            labels = item.get('labels')
            URL = item.get('URL')

            row = [ID, create_date, title, labels, URL]

            file_writer.writerow(row)

if __name__ == '__main__':
    sys.exit(send_to_csv())