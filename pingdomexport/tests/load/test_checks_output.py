import sys
from pingdomexport.load import checks_output

def test_load(capsys):
    checks_output.load(
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
    assert out[0] == 'Id,Name,Created at,Status,Hostname,Type\r\n2057736,A,1458372620,up,www.a.com,http\r\n2057910,B,1458398619,up,b.a.com,http\r\n'
    assert out[1] == ''
