import tablib

class Output:
    def preLoad(self):
        data = tablib.Dataset(
            headers = [
                'Time',
                'Probe ID',
                'Status',
                'Status description',
                'Status long description',
                'Response time'
            ]
        )
        print(data.csv, end="")

    def load(self, results):
        data = tablib.Dataset()
        for result in results:
            data.append(
                [
                    result['time'],
                    result['probeid'],
                    result['status'],
                    result['statusdesc'],
                    result['statusdesclong'],
                    result['responsetime']
                ]
            )
        print(data.csv, end="")
