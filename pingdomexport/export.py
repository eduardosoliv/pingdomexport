import requests
import json
import yaml
import sys
from pingdomexport import configuration
from pingdomexport import pingdom
from pingdomexport import checks
from pingdomexport.load import load_checks

class Export:
    def __init__(self, export_type = 'all', config_path = None):
        try:
            config = configuration.Configuration(config_path)
        except yaml.YAMLError as exc:
            sys.exit("Unable to read configuration: " + str(exc))
        except FileNotFoundError as exc:
            sys.exit(exc)

        self.__pingdom = pingdom.Pingdom(config.pingdom_access())
        self.__config = config
        self.__export_type = export_type

    def run(self):
        filtered_checks = checks.Picker(self.__config.checks(), self.__pingdom.checks()).filter()
        if self.__export_type == 'all' or self.__export_type == 'checks':
            load_checks.load(self.__config, filtered_checks)
