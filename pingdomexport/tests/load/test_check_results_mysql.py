from pingdomexport.load import check_results_mysql

from unittest.mock import Mock, call

class TestMySQL:
    def test_load(self):
        db = Mock()
        check_results_mysql.MySQL(db).load(
            2057736,
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 582,
                    'probeid': 50,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376174
                },
                {
                    'statusdesclong': 'OK',
                    'responsetime': 1420,
                    'probeid': 34,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376114
                }
            ]
        )
        assert 2 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('REPLACE INTO pingdom_check_result (`check_id`, `at`, `probe_id`, `status`, `status_desc`, `status_desc_long`, `response_time`)                VALUES (:check_id, FROM_UNIXTIME(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)', check_id=2057736, at=1458376174, probe_id=50, status='up', status_desc='OK', status_desc_long='OK', response_time=582)
        arg2 = call('REPLACE INTO pingdom_check_result (`check_id`, `at`, `probe_id`, `status`, `status_desc`, `status_desc_long`, `response_time`)                VALUES (:check_id, FROM_UNIXTIME(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)', check_id=2057736, at=1458376114, probe_id=34, status='up', status_desc='OK', status_desc_long='OK', response_time=1420)
        assert args == [arg1, arg2]
