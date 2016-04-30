class Postgres:
    def __init__(self, db):
        self.__db = db

    def load(self, checks):
        for check in checks:
            check_exists = len(self.__db.query('SELECT id FROM pingdom_check WHERE id = :id', id=check['id']).all()) == 1
            if (check_exists):
                self.__db.query(
                    'UPDATE pingdom_check\
                    SET name=:name, created_at=to_timestamp(:created_at), status=:status, hostname=:hostname, type=:type\
                    WHERE id=:id',
                    id=check['id'],
                    name=check['name'],
                    created_at=check['created'],
                    status=check['status'],
                    hostname=check['hostname'],
                    type=check['type']
                )
            else:
                self.__db.query(
                    'INSERT INTO pingdom_check (id, name, created_at, status, hostname, type)\
                    VALUES (:id, :name, to_timestamp(:created_at), :status, :hostname, :type)',
                    id=check['id'],
                    name=check['name'],
                    created_at=check['created'],
                    status=check['status'],
                    hostname=check['hostname'],
                    type=check['type']
                )
