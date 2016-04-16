class MySQL:
    def __init__(self, db):
        self.__db = db

    def load(self, checks):
        for check in checks:
            self.__db.query(
                'REPLACE INTO pingdom_check (`id`, `name`, `created_at`, `status`, `hostname`, `type`)\
                VALUES (:id, :name, FROM_UNIXTIME(:created_at), :status, :hostname, :type)',
                id=check['id'],
                name=check['name'],
                created_at=check['created'],
                status=check['status'],
                hostname=check['hostname'],
                type=check['type']
            )
