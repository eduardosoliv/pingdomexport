import tablib

class Output:
    def pre_load(self):
        data = tablib.Dataset(
            headers=[
                'Check ID',
                'Time',
                'Probe ID',
                'Status',
                'Status description',
                'Status long description',
                'Response time'
            ]
        )
        print(data.csv, end="")

    def load(self, check_id, results):
        data = tablib.Dataset()
        for result in results:
            responsetime = result.get('responsetime', 'n/a')
            data.append(
                [
                    check_id,
                    result['time'],
                    result['probeid'],
                    result['status'],
                    result['statusdesc'],
                    result['statusdesclong'],
                    responsetime
                ]
            )
        print(data.csv, end="")
