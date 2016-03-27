import time
from pingdomexport.load import check_results_output
from pingdomexport import utils

class Load:
    def __init__(self, pingdom):
        self.__pingdom = pingdom
        # @todo use config to understand what to call
        self.__output = check_results_output.Output()

    def load(self, checks, c_to = None):
        for check in checks:
            self.results(check, c_to)

    def results(self, check, c_to = None):
        c_id = check['id']
        c_from = check['created']
        c_to = int(time.time()) if c_to is None else c_to
        intervals = utils.intervals(c_from, c_to)
        for interval in intervals:
            self.__output.load(
                self.__pingdom.check_results(c_id, interval[0], interval[1])
            )
