import records

from pingdomexport.load import checks_mysql
from unittest.mock import MagicMock, Mock, call

class TestOutput:
    def test_load(self):
        db = Mock()
        checks_mysql.MySQL(db).load(
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
        arg1 = call('REPLACE INTO pingdom_check (`id`, `name`, `created_at`, `status`, `hostname`, `type`)                VALUES (:id, :name, FROM_UNIXTIME(:created_at), :status, :hostname, :type)', created_at=1458372620, type='http', hostname='www.a.com', status='up', id=2057736, name='A')
        arg2 = call('REPLACE INTO pingdom_check (`id`, `name`, `created_at`, `status`, `hostname`, `type`)                VALUES (:id, :name, FROM_UNIXTIME(:created_at), :status, :hostname, :type)', hostname='b.a.com', created_at=1458398619, status='up', id=2057910, type='http', name='B')
        assert args == [arg1, arg2]
