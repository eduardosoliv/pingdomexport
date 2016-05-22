import records
from unittest.mock import Mock, call
from pingdomexport.load import check_results_postgres

class TestPostgres:
    def test_load_new(self):
        db = Mock()
        query = Mock()
        query.all.return_value = []
        db.query.return_value = query
        check_results_postgres.Postgres(db).load(
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
        assert 4 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('SELECT id FROM pingdom_check_result WHERE check_id = :check_id AND at = to_timestamp(:at) AND probe_id = :probe_id', check_id=2057736, at=1458376174, probe_id=50)
        arg2 = call('INSERT INTO pingdom_check_result (check_id, at, probe_id, status, status_desc, status_desc_long, response_time)                    VALUES (:check_id, to_timestamp(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)', check_id=2057736, at=1458376174, probe_id=50, status='up', status_desc='OK', status_desc_long='OK', response_time=582)
        arg3 = call('SELECT id FROM pingdom_check_result WHERE check_id = :check_id AND at = to_timestamp(:at) AND probe_id = :probe_id', check_id=2057736, at=1458376114, probe_id=34)
        arg4 = call('INSERT INTO pingdom_check_result (check_id, at, probe_id, status, status_desc, status_desc_long, response_time)                    VALUES (:check_id, to_timestamp(:at), :probe_id, :status, :status_desc, :status_desc_long, :response_time)', check_id=2057736, at=1458376114, probe_id=34, status='up', status_desc='OK', status_desc_long='OK', response_time=1420)
        assert args == [arg1, arg2, arg3, arg4]

    def test_load_existent(self):
        db = Mock()
        query = Mock()
        query.all.return_value = [records.Record(['id'], [1])]
        db.query.return_value = query
        check_results_postgres.Postgres(db).load(
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
        assert 4 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('SELECT id FROM pingdom_check_result WHERE check_id = :check_id AND at = to_timestamp(:at) AND probe_id = :probe_id', check_id=2057736, at=1458376174, probe_id=50)
        arg2 = call('UPDATE pingdom_check_result                    SET check_id=:check_id, at=to_timestamp(:at), probe_id=:probe_id, status=:status, status_desc=:status_desc, status_desc_long=:status_desc_long, response_time=:response_time                    WHERE id=:id', check_id=2057736, at=1458376174, probe_id=50, status='up', status_desc='OK', status_desc_long='OK', response_time=582, id=1)
        arg3 = call('SELECT id FROM pingdom_check_result WHERE check_id = :check_id AND at = to_timestamp(:at) AND probe_id = :probe_id', check_id=2057736, at=1458376114, probe_id=34)
        arg4 = call('UPDATE pingdom_check_result                    SET check_id=:check_id, at=to_timestamp(:at), probe_id=:probe_id, status=:status, status_desc=:status_desc, status_desc_long=:status_desc_long, response_time=:response_time                    WHERE id=:id', check_id=2057736, at=1458376114, probe_id=34, status='up', status_desc='OK', status_desc_long='OK', response_time=1420, id=1)
        assert args == [arg1, arg2, arg3, arg4]
