import tablib

class Output:
    def load(self, checks):
        data = tablib.Dataset(headers=['Id', 'Name', 'Created at', 'Status', 'Hostname', 'Type'])
        for check in checks:
            data.append(
                [
                    check['id'],
                    check['name'],
                    check['created'],
                    check['status'],
                    check['hostname'],
                    check['type'],
                ]
            )
        print(data.csv, end="")
