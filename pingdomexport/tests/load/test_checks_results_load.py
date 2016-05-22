from unittest.mock import MagicMock, Mock, call
from pingdomexport.load import checks_results_load
from pingdomexport import configuration

class TestLoad:
    def test_output_load(self, capsys):
        config = configuration.Load('output', {})
        pingdom = Mock()
        pingdom.check_results.side_effect = [
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376174
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376175
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376176
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376177
                    }
                ]
            }
        ]
        checks_results_load.Load(config, pingdom).load(
            [
                {
                    "id": 2057736,
                    "created": 1458372620
                },
                {
                    "id": 2057737,
                    "created": 1458372620
                }
            ],
            c_to=1458372620 + 3600 * 2
        )

        assert 4 == pingdom.check_results.call_count
        out = capsys.readouterr()
        assert len(out) == 2
        assert 'Check ID,Time,Probe ID,Status,Status description,Status long description,Response time\r\n2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376175,50,up,OK,OK,582\r\n2057737,1458376176,50,up,OK,OK,582\r\n2057737,1458376177,50,up,OK,OK,582\r\n' == out[0]
        assert '' == out[1]

    def test_output_load_results(self, capsys):
        config = configuration.Load('output', {})
        pingdom = Mock()
        pingdom.check_results = MagicMock(
            return_value={
                "results": [
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
            }
        )
        checks_results_load.Load(config, pingdom).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            c_to=1458372620 + 100
        )

        pingdom.check_results.assert_called_with(2057736, 1458372620, 1458372720)
        out = capsys.readouterr()
        assert len(out) == 2
        assert '2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]

    def test_output_load_results_with_from(self, capsys):
        config = configuration.Load('output', {})
        created = 1458372620
        pingdom = Mock()
        pingdom.check_results = MagicMock(return_value={"results": []})
        checks_results_load.Load(config, pingdom).results(
            {
                "id": 2057736,
                "created": created
            },
            created + 100,
            created + 1000
        )

        pingdom.check_results.assert_called_with(2057736, created + 100, created + 1000)

    def test_output_load_results_invalid_from(self):
        config = configuration.Load('output', {})
        created = 1458372620
        pingdom = Mock()
        pingdom.check_results = MagicMock(return_value={"results": []})
        checks_results_load.Load(config, pingdom).results(
            {
                "id": 2057736,
                "created": created
            },
            created - 100,
            created + 1000
        )

        pingdom.check_results.assert_called_with(2057736, created, created + 1000)

    def test_output_load_results_multi(self, capsys):
        config = configuration.Load('output', {})
        pingdom = Mock()
        pingdom.check_results.side_effect = [
            {
                "results": [
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
                        'responsetime': 682,
                        'probeid': 51,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376184
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 1420,
                        'probeid': 34,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376114
                    }
                ]
            }
        ]
        checks_results_load.Load(config, pingdom).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            c_to=1458372620 + 3600 * 2
        )

        assert 2 == pingdom.check_results.call_count
        out = capsys.readouterr()
        assert len(out) == 2
        assert '2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376184,51,up,OK,OK,682\r\n2057736,1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]

    def test_mysql_load(self):
        config = Mock()
        db = Mock()
        config.is_type_db.return_value = True
        config.is_type_mysql.return_value = True
        config.db_connection.return_value = db

        pingdom = Mock()
        pingdom.check_results.side_effect = [
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376174
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376175
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376176
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376177
                    }
                ]
            }
        ]
        checks_results_load.Load(config, pingdom).load(
            [
                {
                    "id": 2057736,
                    "created": 1458372620
                },
                {
                    "id": 2057737,
                    "created": 1458372620
                }
            ],
            c_to=1458372620 + 3600 * 2
        )

        assert 4 == db.query.call_count

    def test_posgres_load(self):
        config = Mock()

        db = Mock()
        query = Mock()
        query.all.return_value = []
        db.query.return_value = query

        config.is_type_db.return_value = True
        config.is_type_mysql.return_value = False
        config.is_type_postgres.return_value = True
        config.db_connection.return_value = db

        pingdom = Mock()
        pingdom.check_results.side_effect = [
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376174
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376175
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376176
                    }
                ]
            },
            {
                "results": [
                    {
                        'statusdesclong': 'OK',
                        'responsetime': 582,
                        'probeid': 50,
                        'status': 'up',
                        'statusdesc': 'OK',
                        'time': 1458376177
                    }
                ]
            }
        ]
        checks_results_load.Load(config, pingdom).load(
            [
                {
                    "id": 2057736,
                    "created": 1458372620
                },
                {
                    "id": 2057737,
                    "created": 1458372620
                }
            ],
            c_to=1458372620 + 3600 * 2
        )

        assert 8 == db.query.call_count
