import time
from pingdomexport.load import check_results_output, check_results_mysql, check_results_postgres
from pingdomexport import utils

class Load:
    def __init__(self, config, pingdom):
        self.__pingdom = pingdom
        self.__config = config
        self.__output = check_results_output.Output()
        if config.is_type_db():
            db_connection = config.db_connection();
            if config.is_type_mysql():
                self.__output = check_results_mysql.MySQL(db_connection)
            else:
                self.__output = check_results_postgres.Postgres(db_connection)

    def load(self, checks, c_from=None, c_to=None):
        self.__output.pre_load()
        for check in checks:
            self.results(check, c_from, c_to)

    def results(self, check, c_from=None, c_to=None):
        c_id = check['id']
        c_from = c_from if c_from and c_from > check['created'] else check['created']
        c_to = int(time.time()) if c_to is None else c_to
        intervals = utils.intervals(c_from, c_to)
        for interval in intervals:
            check_results = self.__pingdom.check_results(c_id, interval[0], interval[1])
            self.__output.load(c_id, check_results.get('results', []))
