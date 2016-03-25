import requests
import json
import yaml
import sys
from pingdomexport import configuration
from pingdomexport import pingdom
from pingdomexport import checks

class Export:
    def __init__(self):
        try:
            self.__config = configuration.Configuration()
        except yaml.YAMLError as exc:
            sys.exit("Unable to read configuration: " + str(exc))
        except FileNotFoundError as exc:
            sys.exit(exc)

        self.__pingdom = pingdom.Pingdom(self.__config.pingdom_access())

    def getChecks(self):
        return checks.Picker(self.__config.checks(), self.__pingdom.checks()).get()
