import requests
import json
import yaml
import sys
from pingdomexport import configuration, pingdom, checks
from pingdomexport.load import checks_load, checks_results_load

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
        if self.__export_type in ['all', 'checks']:
            checks_load.Load(self.__config).load(filtered_checks)
        if self.__export_type in ['all', 'results']:
            checks_results_load.Load(self.__config, self.__pingdom).load(filtered_checks)
