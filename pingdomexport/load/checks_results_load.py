import time
from pingdomexport.load import check_results_output
from pingdomexport import utils

class Load:
    def __init__(self, config, pingdom):
        self.__pingdom = pingdom
        self.__config = config
        # @todo use config to understand what to call
        self.__output = check_results_output.Output()

    def load(self, checks, c_to = None):
        self.__output.preLoad()
        for check in checks:
            self.results(check, c_to)

    def results(self, check, c_to = None):
        c_id = check['id']
        c_from = check['created']
        c_to = int(time.time()) if c_to is None else c_to
        intervals = utils.intervals(c_from, c_to)
        for interval in intervals:
            check_results = self.__pingdom.check_results(c_id, interval[0], interval[1]);
            self.__output.load(check_results.get('results', []))
