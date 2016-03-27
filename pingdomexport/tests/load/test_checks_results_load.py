from unittest.mock import MagicMock, Mock
from pingdomexport.load import checks_results_load

class TestLoad:
    def test_load(self, capsys):
        mock = Mock()
        mock.check_results.side_effect = [
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
        checks_results_load.Load("config", mock).load(
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

        assert 4 == mock.check_results.call_count
        out = capsys.readouterr()
        assert len(out) == 2
        assert 'Check ID,Time,Probe ID,Status,Status description,Status long description,Response time\r\n2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376175,50,up,OK,OK,582\r\n2057737,1458376176,50,up,OK,OK,582\r\n2057737,1458376177,50,up,OK,OK,582\r\n' == out[0]
        assert '' == out[1]

    def test_load_results(self, capsys):
        mock = Mock()
        mock.check_results = MagicMock(
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
        checks_results_load.Load("config", mock).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            c_to=1458372620 + 100
        )

        mock.check_results.assert_called_with(2057736, 1458372620, 1458372720)
        out = capsys.readouterr()
        assert len(out) == 2
        assert '2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]

    def test_load_results_with_from(self, capsys):
        created = 1458372620
        mock = Mock()
        mock.check_results = MagicMock(return_value={"results": []})
        checks_results_load.Load("config", mock).results(
            {
                "id": 2057736,
                "created": created
            },
            created + 100,
            created + 1000
        )

        mock.check_results.assert_called_with(2057736, created + 100, created + 1000)

    def test_load_results_invalid_from(self):
        created = 1458372620
        mock = Mock()
        mock.check_results = MagicMock(return_value={"results": []})
        checks_results_load.Load("config", mock).results(
            {
                "id": 2057736,
                "created": created
            },
            created - 100,
            created + 1000
        )

        mock.check_results.assert_called_with(2057736, created, created + 1000)

    def test_load_results_multi(self, capsys):
        mock = Mock()
        mock.check_results.side_effect = [
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
        checks_results_load.Load("config", mock).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            c_to=1458372620 + 3600 * 2
        )

        assert 2 == mock.check_results.call_count
        out = capsys.readouterr()
        assert len(out) == 2
        assert '2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376184,51,up,OK,OK,682\r\n2057736,1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]
