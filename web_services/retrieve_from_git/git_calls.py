BASE_URL = 'https://api.github.com/'
BLOCKER_ISSUES = BASE_URL + \
    'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
    'label:prio:blocker+-label:customer_reported+state:open'
HIGH_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:high+-label:customer_reported+state:open'
NORMAL_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:normal+-label:customer_reported+state:open'
LOW_ISSUES = BASE_URL + \
        'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
        'label:prio:low+-label:customer_reported+state:open'
CUSTOMER_REPORTED_ISSUES = \
    BASE_URL + \
    'search/issues?q=repo:artemishealth/artemis-app+label:bug+' \
    'label:customer_reported+state:open'


# TODO - Replace below with a token.
USERNAME = 'My User Name'
PASSWORD = 'My Password'
