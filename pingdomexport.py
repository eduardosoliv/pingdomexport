import json
import requests
import argparse
import sys
from pingdomexport import export

parser = argparse.ArgumentParser()
parser.add_argument(
    "--type",
    help="Export type if only the check list or the results, options: checks|results|all"
)
parser.add_argument(
    "--config",
    help="The path to the configuration, if not provided will search config.yml"
)
args = parser.parse_args()

export_type = 'all'
if args.type:
    if args.type not in ['checks', 'results', 'all']:
        print("Invalid export type, must be: checks|results|all")
        sys.exit()
    export_type = args.type

export.Export(export_type, args.config).run()
