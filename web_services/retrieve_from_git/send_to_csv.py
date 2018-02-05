import csv
import sys
import web_services.retrieve_from_git.git_blocker_issues as blockers
import web_services.retrieve_from_git.git_blocker_issues_open_closed as blockers_rolling_avg
import web_services.retrieve_from_git.git_issues_customer_reported as customer_reported
import web_services.retrieve_from_git.git_issues_internal as internal_reported


def send_to_csv():
    internal_data = internal_reported.sort_by_year_month()
    customer_data = customer_reported.sort_by_year_month()
    blocker_data = blockers.sort_by_year_month()
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
        for date in internal_data:
            row = [date, avg]
            for key, internal_value in internal_data[date].items():
                row.append(internal_value)
            for customer_issue in customer_data:
                for key, customer_value in customer_data[customer_issue].items():
                    row.append(customer_value)
            for blocker_issue in blocker_data:
                for key, blocker_value in blocker_data[blocker_issue].items():
                    row.append(blocker_value)
        file_writer.writerow(row)


if __name__ == '__main__':
    sys.exit(send_to_csv())

