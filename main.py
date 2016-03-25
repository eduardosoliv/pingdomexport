import json
from pingdomexport import export

export = export.Export()
checks = export.getChecks()
print(json.dumps(checks, sort_keys=True, indent=4, separators=(',', ': ')))
