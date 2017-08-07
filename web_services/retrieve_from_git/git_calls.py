BASE_URL = 'https://api.github.com/'
HIGH_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:high+-label:customer_reported+state:open&sort=created&order=asc'
NORMAL_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:normal+-label:customer_reported+state:open&sort=created&order=asc'
LOW_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:low+-label:customer_reported+state:open&sort=created&order=asc'
CUSTOMER_REPORTED_ISSUES = \
    BASE_URL + \
    'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
    'label:customer_reported+state:open&sort=created&order=asc'
BLOCKER_ISSUES = BASE_URL + \
    'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
    'label:prio:blocker+-label:customer_reported+state:open&sort=created&order=asc'

# TODO - Replace below with a token.
USERNAME = 'MY USER'
PASSWORD = 'MY PASSWORD'
