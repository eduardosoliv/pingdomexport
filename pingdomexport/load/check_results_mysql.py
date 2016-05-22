class MySQL:
    def __init__(self, db):
        self.__db = db

    def pre_load(self):
        # do nothing
        return

    def load(self, check_id, results):
        for result in results:
            responsetime = result.get('responsetime', None)
            self.__db.query(
                'REPLACE INTO pingdom_check_result (`check_id`, `at`, `probe_id`, `status`, `status_desc`, `status_desc_long`, `response_time`)\
                VALUES (:check_id, FROM_UNIXTIME(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)',
                check_id=check_id,
                at=result['time'],
                probe_id=result['probeid'],
                status=result['status'],
                status_desc=result['statusdesc'],
                status_desc_long=result['statusdesclong'],
                response_time=responsetime
            )
