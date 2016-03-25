import yaml
import os.path
from typing import Dict
from typing import List

class PingdomAccess:
    def __init__(
        self,
        username: str,
        password: str,
        account_email: str,
        app_key: str
    ):
        self.__username = username
        self.__password = password
        self.__account_email = account_email
        self.__app_key = app_key

    @classmethod
    def from_dict(config, data: Dict[str, int]):
        return config(
            data['username'],
            data['password'],
            data['account_email'],
            data['app_key']
        )

    def username(self):
        return self.__username
    def password(self):
        return self.__password
    def account_email(self):
        return self.__account_email
    def app_key(self):
        return self.__app_key

class Checks:
    def __init__(self, strategy: str, ids: List[int]):
        if strategy not in ['all', 'include', 'exclude']:
            raise ValueError("Checks configuration strategy must be all/include/exclude")
        if strategy == 'all' and len(ids) != 0:
            raise ValueError('Checks configuration ids must be empty when strategy is all')
        self.__strategy = strategy
        self.__ids = ids

    @classmethod
    def from_dict(config, data: Dict[str, int]):
        return config(
            data['strategy'],
            data['ids']
        )

    def strategy(self):
        return self.__strategy
    def is_strategy_all(self):
        return self.strategy() == 'all'
    def is_strategy_include(self):
        return self.strategy() == 'include'
    def is_strategy_exclude(self):
        return self.strategy() == 'exclude'
    def ids(self):
        return self.__ids

class Configuration:
    def __init__(self, config_path = None):
        if (config_path is None):
            config_path =  os.path.dirname(os.path.realpath(__file__)) + '/../config.yml'

        if not os.path.isfile(config_path):
            raise FileNotFoundError("Config " + config_path + " not found")

        with open(config_path, 'r') as stream:
            config = yaml.load(stream)

        self.__pingdom_access = PingdomAccess.from_dict(config['pingdom_access'])
        self.__checks = Checks.from_dict(config['checks'])

    def pingdom_access(self):
        return self.__pingdom_access

    def checks(self):
        return self.__checks
