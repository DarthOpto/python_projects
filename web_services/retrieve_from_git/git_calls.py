BASE_URL = 'https://api.github.com/'
OPEN_ISSUES = BASE_URL + 'repos/artemishealth/artemis-app/issues?state=open&labels=bug&page={}'
CUSTOMER_REPORTED = BASE_URL + 'repos/artemishealth/artemis-app/issues?state=all&labels=bug,customer%20reported&page={}'
BLOCKER_BUGS = BASE_URL + 'repos/artemishealth/artemis-app/issues?state=all&labels=bug,severity:%20critical&page={}'
CLOSED_BLOCKER_BUGS = BASE_URL + \
                      'repos/artemishealth/artemis-app/issues?state=closed&labels=bug,severity:%20critical&page={}'


# TODO - Replace below with a token.
USERNAME = 'DarthOpto'
PASSWORD = 'M1ckeyM0use'
