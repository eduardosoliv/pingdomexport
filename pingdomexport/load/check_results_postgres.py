class Postgres:
    def __init__(self, db):
        self.__db = db

    def pre_load(self):
        # do nothing
        return

    def load(self, check_id, results):
        for result in results:
            responsetime = result.get('responsetime', None)
            rows = self.__db.query(
                'SELECT id FROM pingdom_check_result WHERE check_id = :check_id AND at = to_timestamp(:at) AND probe_id = :probe_id',
                check_id=check_id,
                at=result['time'],
                probe_id=result['probeid']
            )
            rows = rows.all()
            check_exists = len(rows) == 1
            if (check_exists):
                self.__db.query(
                    'UPDATE pingdom_check_result\
                    SET check_id=:check_id, at=to_timestamp(:at), probe_id=:probe_id, status=:status, status_desc=:status_desc, status_desc_long=:status_desc_long, response_time=:response_time\
                    WHERE id=:id',
                    check_id=check_id,
                    at=result['time'],
                    probe_id=result['probeid'],
                    status=result['status'],
                    status_desc=result['statusdesc'],
                    status_desc_long=result['statusdesclong'],
                    response_time=responsetime,
                    id=rows[0].id
                )
            else:
                self.__db.query(
                    'INSERT INTO pingdom_check_result (check_id, at, probe_id, status, status_desc, status_desc_long, response_time)\
                    VALUES (:check_id, to_timestamp(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)',
                    check_id=check_id,
                    at=result['time'],
                    probe_id=result['probeid'],
                    status=result['status'],
                    status_desc=result['statusdesc'],
                    status_desc_long=result['statusdesclong'],
                    response_time=responsetime
                )
