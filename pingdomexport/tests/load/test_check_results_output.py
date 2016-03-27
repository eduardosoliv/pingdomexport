from pingdomexport.load import check_results_output

class TestOutput:
    def test_pre_load(self, capsys):
        check_results_output.Output().pre_load()

        out = capsys.readouterr()
        assert len(out) == 2
        assert 'Check ID,Time,Probe ID,Status,Status description,Status long description,Response time\r\n' == out[0]
        assert '' == out[1]

    def test_load(self, capsys):
        check_results_output.Output().load(
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

        out = capsys.readouterr()
        assert len(out) == 2
        assert '2057736,1458376174,50,up,OK,OK,582\r\n2057736,1458376114,34,up,OK,OK,1420\r\n' == out[0]
        assert '' == out[1]
