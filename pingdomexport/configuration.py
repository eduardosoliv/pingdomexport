import os.path
import yaml
import records

class PingdomAccess:
    def __init__(self, username, password, account_email, app_key):
        self.__username = username
        self.__password = password
        self.__account_email = account_email
        self.__app_key = app_key

    @classmethod
    def from_dict(cls, data):
        return cls(
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
    def __init__(self, strategy, ids):
        if strategy not in ['all', 'include', 'exclude']:
            raise ValueError("Checks configuration strategy must be all/include/exclude")
        if strategy == 'all' and len(ids) != 0:
            raise ValueError('Checks configuration ids must be empty when strategy is all')
        self.__strategy = strategy
        self.__ids = ids

    @classmethod
    def from_dict(cls, data):
        return cls(
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

class Load:
    def __init__(self, type, params):
        if type not in ['output', 'mysql', 'postgres']:
            raise ValueError("Load configuration type must be output/mysql/postgres")
        if type == 'output' and params:
            raise ValueError("On load configuration type output parameters are not expected")
        if type in ['mysql', 'postgres'] and 'db_url' not in params:
            raise ValueError("On load configuration type mysql/postgres db_url parameter is expected")
        self.__type = type
        self.__params = params

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['type'],
            data['parameters']
        )

    def type(self):
        return self.__type

    def params(self):
        return self.__params

    def is_type_output(self):
        return self.type() == 'output'
    def is_type_mysql(self):
        return self.type() == 'mysql'
    def is_type_postgres(self):
        return self.type() == 'postgres'
    def is_type_db(self):
        return not self.is_type_output()

    def db_connection(self):
        db_connection = None
        if (self.is_type_db):
            db_connection = records.Database(self.params()['db_url'])
        return db_connection

class Configuration:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.dirname(os.path.realpath(__file__)) + '/../config.yml'

        if not os.path.isfile(config_path):
            raise FileNotFoundError("Config " + config_path + " not found")

        with open(config_path, 'r') as stream:
            config = yaml.load(stream)

        self.__pingdom_access = PingdomAccess.from_dict(config['pingdom_access'])
        self.__checks = Checks.from_dict(config['checks'])
        self.__load = Load.from_dict(config['load'])

    def pingdom_access(self):
        return self.__pingdom_access

    def checks(self):
        return self.__checks

    def load(self):
        return self.__load
