class Picker:
    def __init__(self, config, checks):
        self.__config = config
        self.__checks = checks

    def filter(self):
        checks = self.__checks['checks']
        if self.__config.is_strategy_include():
            checks = self.__include(checks)
        elif self.__config.is_strategy_exclude():
            checks = self.__exclude(checks)
        return checks

    def __include(self, checks):
        filtered_checks = []
        for check in checks:
            if check['id'] in self.__config.ids():
                filtered_checks.append(check)
        return filtered_checks

    def __exclude(self, checks):
        filtered_checks = []
        for check in checks:
            if check['id'] not in self.__config.ids():
                filtered_checks.append(check)
        return filtered_checks
