from pingdomexport.load import checks_output

class Load:
    def __init__(self, config):
        self.__config = config
        # @todo use config to understand what to call
        self.__output = checks_output.Output()

    def load(self, checks):
        self.__output.load(checks)
