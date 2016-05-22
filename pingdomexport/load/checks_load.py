import records
from pingdomexport.load import checks_output, checks_mysql, checks_postgres

class Load:
    def __init__(self, config):
        self.__config = config
        self.__output = checks_output.Output()
        if config.is_type_db():
            db_connection = config.db_connection();
            if config.is_type_mysql():
                self.__output = checks_mysql.MySQL(db_connection)
            else:
                self.__output = checks_postgres.Postgres(db_connection)

    def load(self, checks):
        self.__output.load(checks)
