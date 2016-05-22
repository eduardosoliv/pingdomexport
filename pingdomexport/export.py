from pingdomexport import configuration, pingdom, checks
from pingdomexport.load import checks_load, checks_results_load

class Export:
    def __init__(self, export_type='all', config_path=None, checks_from=None, checks_to=None):
        if export_type not in ['checks', 'results', 'all']:
            raise ValueError('Invalid export type, must be: checks|results|all')
        config = configuration.Configuration(config_path)

        self.__pingdom = pingdom.Pingdom(config.pingdom_access())
        self.__config = config
        self.__export_type = export_type
        self.__checks_from = checks_from
        self.__checks_to = checks_to

    def run(self):
        filtered_checks = checks.Picker(self.__config.checks(), self.__pingdom.checks()).filter()
        if self.__export_type in ['all', 'checks']:
            checks_load.Load(self.__config.load()).load(filtered_checks)
        if self.__export_type in ['all', 'results']:
            checks_results_load.Load(self.__config.load(), self.__pingdom).load(
                filtered_checks,
                self.__checks_from,
                self.__checks_to
            )
