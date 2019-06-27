### How to use this!

Using the API given below create an automated test with the listed acceptance criteria:

 

## API = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false

 

## Acceptance Criteria:

1. Name = "Carbon credits"
1. CanRelist = true
1. The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

## Instructions:

Your test needs to be written using a programming language of your choice (not a tool like SoapUI). Ensure you include a clear ReadMe
Submit your test to us in a format that lets us execute and review the code (it must be submitted in a public repository like Bitbucket or Github)
Your test must validate all the three acceptance criteria
Points will be awarded for meeting the criteria, style and the use of good practices and appropriate use of source control
We want to see your best work - no lazy coding or comments.

1. ```pip install .```
1. ```pre-commit install --install-hooks```
1. prior to commit ```black .```
1. ```pytest -v --html=assurity_tests_report.html```
1. Move back to New Zealand
