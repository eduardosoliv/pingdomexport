from pingdomexport.load import checks_load
from pingdomexport import configuration
from unittest.mock import Mock, call

class TestLoad:
    def test_output_load(self, capsys):
        config = configuration.Load('output', {})
        checks_load.Load(config).load(
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

        out = capsys.readouterr()
        assert len(out) == 2
        assert 'Id,Name,Created at,Status,Hostname,Type\r\n2057736,A,1458372620,up,www.a.com,http\r\n2057910,B,1458398619,up,b.a.com,http\r\n' == out[0]
        assert '' == out[1]

    def test_mysql_load(self):
        config = Mock()
        db = Mock()
        config.is_type_db.return_value = True
        config.is_type_mysql.return_value = True
        config.db_connection.return_value = db
        checks_load.Load(config).load(
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

        assert 2 == db.query.call_count
        args = db.query.call_args_list
        arg1 = call('REPLACE INTO pingdom_check (`id`, `name`, `created_at`, `status`, `hostname`, `type`)                VALUES (:id, :name, FROM_UNIXTIME(:created_at), :status, :hostname, :type)', id=2057736, name='A', created_at=1458372620, status='up', hostname='www.a.com', type='http')
        arg2 = call('REPLACE INTO pingdom_check (`id`, `name`, `created_at`, `status`, `hostname`, `type`)                VALUES (:id, :name, FROM_UNIXTIME(:created_at), :status, :hostname, :type)', id=2057910, name='B', created_at=1458398619, status='up', hostname='b.a.com', type='http')
        assert args == [arg1, arg2]

    def test_postgres_load(self):
        config = Mock()

        db = Mock()
        query = Mock()
        query.all.return_value = []
        db.query.return_value = query

        config.is_type_db.return_value = True
        config.is_type_mysql.return_value = False
        config.is_type_postgres.return_value = True
        config.db_connection.return_value = db

        checks_load.Load(config).load(
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
