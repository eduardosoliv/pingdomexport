from pingdomexport.load import checks_results_load
from unittest.mock import MagicMock, Mock

class TestLoad:
    def test_load(self, capsys):
        mock = Mock()
        mock.check_results.side_effect = [
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 582,
                    'probeid': 50,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376174
                }
            ],
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 1420,
                    'probeid': 34,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376114
                }
            ],
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 682,
                    'probeid': 51,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376184
                }
            ],
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 682,
                    'probeid': 51,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376184
                }
            ]
        ]
        checks_results_load.Load(mock).load(
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
            1458372620 + 3600 * 2
        )

        assert 4 == mock.check_results.call_count
        #out = capsys.readouterr()
        #assert len(out) == 2
        #assert '1458376174,50,up,OK,OK,582\r\n1458376184,51,up,OK,OK,682\r\n1458376114,34,up,OK,OK,1420\r\n' == out[0]
        #assert '' == out[1]

    def test_load_results(self, capsys):
        mock = Mock()
        mock.check_results = MagicMock(
            return_value=[
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
        checks_results_load.Load(mock).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            1458372620 + 100
        )

        mock.check_results.assert_called_with(2057736, 1458372620, 1458372720)
        out = capsys.readouterr()
        assert len(out) == 2
        assert '1458376174,50,up,OK,OK,582\r\n1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]

    def test_load_results_multi(self, capsys):
        mock = Mock()
        mock.check_results.side_effect = [
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
                    'responsetime': 682,
                    'probeid': 51,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376184
                }
            ],
            [
                {
                    'statusdesclong': 'OK',
                    'responsetime': 1420,
                    'probeid': 34,
                    'status': 'up',
                    'statusdesc': 'OK',
                    'time': 1458376114
                }
            ]
        ]
        checks_results_load.Load(mock).results(
            {
                "id": 2057736,
                "created": 1458372620
            },
            1458372620 + 3600 * 2
        )

        assert 2 == mock.check_results.call_count
        out = capsys.readouterr()
        assert len(out) == 2
        assert '1458376174,50,up,OK,OK,582\r\n1458376184,51,up,OK,OK,682\r\n1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]
