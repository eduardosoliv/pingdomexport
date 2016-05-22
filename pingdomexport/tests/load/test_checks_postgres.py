import records
from pingdomexport.load import checks_postgres
from unittest.mock import Mock, call

class TestPostgres:
    def test_load_new(self):
        db = Mock()
        query = Mock()
        query.all.return_value = []
        db.query.return_value = query
        checks_postgres.Postgres(db).load(
            [
                {
                    'hostname': 'www.a.com',
                    'use_legacy_notifications': True,
                    'lastresponsetime': 411,
                    'ipv6': False,
                    'type': 'http',
                    'name': 'A',
                    'resolution': 1,
                    'created': 1458372620,
                    'lasttesttime': 1459005934,
                    'status': 'up',
                    'id': 2057736
                },
                {
                    'lasterrortime': 1458938840,
                    'type': 'http',
                    'hostname': 'b.a.com',
                    'lastresponsetime': 827,
                    'created': 1458398619,
                    'lasttesttime': 1459005943,
                    'status': 'up',
                    'ipv6': False,
                    'use_legacy_notifications': True,
                    'resolution': 1,
                    'name': 'B',
                    'id': 2057910
                }
            ]
        )

        assert 4 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('SELECT id FROM pingdom_check WHERE id = :id', id=2057736)
        arg2 = call('INSERT INTO pingdom_check (id, name, created_at, status, hostname, type)                    VALUES (:id, :name, to_timestamp(:created_at), :status, :hostname, :type)', id=2057736, name='A', created_at=1458372620, status='up', hostname='www.a.com', type='http')
        arg3 = call('SELECT id FROM pingdom_check WHERE id = :id', id=2057910)
        arg4 = call('INSERT INTO pingdom_check (id, name, created_at, status, hostname, type)                    VALUES (:id, :name, to_timestamp(:created_at), :status, :hostname, :type)', id=2057910, name='B', created_at=1458398619, status='up', hostname='b.a.com', type='http')
        assert args == [arg1, arg2, arg3, arg4]

    def test_load_existent(self):
        db = Mock()
        query = Mock()
        query.all.return_value = [records.Record(['id'], [2057736])]
        db.query.return_value = query
        checks_postgres.Postgres(db).load(
            [
                {
                    'hostname': 'www.a.com',
                    'use_legacy_notifications': True,
                    'lastresponsetime': 411,
                    'ipv6': False,
                    'type': 'http',
                    'name': 'A',
                    'resolution': 1,
                    'created': 1458372620,
                    'lasttesttime': 1459005934,
                    'status': 'up',
                    'id': 2057736
                },
                {
                    'lasterrortime': 1458938840,
                    'type': 'http',
                    'hostname': 'b.a.com',
                    'lastresponsetime': 827,
                    'created': 1458398619,
                    'lasttesttime': 1459005943,
                    'status': 'up',
                    'ipv6': False,
                    'use_legacy_notifications': True,
                    'resolution': 1,
                    'name': 'B',
                    'id': 2057910
                }
            ]
        )

        assert 4 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('SELECT id FROM pingdom_check WHERE id = :id', id=2057736)
        arg2 = call('UPDATE pingdom_check                    SET name=:name, created_at=to_timestamp(:created_at), status=:status, hostname=:hostname, type=:type                    WHERE id=:id', id=2057736, name='A', created_at=1458372620, status='up', hostname='www.a.com', type='http')
        arg3 = call('SELECT id FROM pingdom_check WHERE id = :id', id=2057910)
        arg4 = call('UPDATE pingdom_check                    SET name=:name, created_at=to_timestamp(:created_at), status=:status, hostname=:hostname, type=:type                    WHERE id=:id', id=2057910, name='B', created_at=1458398619, status='up', hostname='b.a.com', type='http')
        assert args == [arg1, arg2, arg3, arg4]
