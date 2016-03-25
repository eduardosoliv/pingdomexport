import pytest
import requests
import requests_mock
import base64
import sys
from pingdomexport import configuration, pingdom

class TestPingdom:
    def test_successful_construction(self):
        pingdom.Pingdom(
            configuration.PingdomAccess('u', 'p', 'ae', 'akey')
        )

    def test_checks(self):
        with requests_mock.mock() as m:
            p = pingdom.Pingdom(
                configuration.PingdomAccess('u', 'p', 'ae', 'akey')
            )
            m.get(
                'https://api.pingdom.com/api/2.0/checks',
                request_headers={
                    'Authorization': 'Basic dTpw',
                    'App-Key': 'akey',
                    'Account-Email': 'ae',
                    'Accept': 'application/json'
                },
                headers = {
                    'Content-Type': 'application/json'
                },
                text="{}"
            )
            assert p.checks() == {}
