import requests

class Pingdom:
    def __init__(self, config):
        self.__headers = {
            'App-Key': config.app_key(),
            'Account-Email': config.account_email(),
            'Accept': 'application/json'
        }
        self.__auth=(config.username(), config.password())

    def checks(self):
        r = self.__rget('checks')
        r.raise_for_status()
        if r.headers.get('content-type') != 'application/json':
            raise RuntimeError('Excepted content type application/json')
        return r.json()

    def __rget(self, uri):
        return requests.get(
            'https://api.pingdom.com/api/2.0/' + uri,
            auth=self.__auth,
            headers=self.__headers
        )
