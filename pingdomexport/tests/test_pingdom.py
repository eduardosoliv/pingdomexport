import pytest
import requests
import requests_mock
import base64
from pingdomexport import configuration, pingdom

class TestPingdom:
    def test_successful_construction(self):
        pingdom.Pingdom(configuration.PingdomAccess('u', 'p', 'ae', 'akey'))

    def test_checks_response_not_json(self):
        with requests_mock.mock() as m:
            with pytest.raises(RuntimeError):
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
                        'Content-Type': 'application/xml'
                    },
                    text="{}"
                )
                p.checks()

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

    def test_check_results_response_not_json(self):
        with requests_mock.mock() as m:
            with pytest.raises(RuntimeError):
                p = pingdom.Pingdom(
                    configuration.PingdomAccess('u', 'p', 'ae', 'akey')
                )
                m.get(
                    'https://api.pingdom.com/api/2.0/results/1?from=1458696400&to=1458700000',
                    request_headers={
                        'Authorization': 'Basic dTpw',
                        'App-Key': 'akey',
                        'Account-Email': 'ae',
                        'Accept': 'application/json'
                    },
                    headers = {
                        'Content-Type': 'application/xml'
                    },
                    text="{}"
                )
                p.check_results(1, 1458696400, 1458700000)

    def test_check_results(self):
        with requests_mock.mock() as m:
            p = pingdom.Pingdom(
                configuration.PingdomAccess('u', 'p', 'ae', 'akey')
            )
            m.get(
                'https://api.pingdom.com/api/2.0/results/1?from=1458696400&to=1458700000',
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
            assert p.check_results(1, 1458696400, 1458700000) == {}
