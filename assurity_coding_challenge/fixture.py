"""
Fixture file for tests to be based on.
"""
import pytest
import json
import requests


@pytest.fixture(scope="module")
def api_call_response():
    response = requests.get(
        "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"
    )
    return json.loads(response.text)
