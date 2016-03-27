import json
import requests
import argparse
import sys
import yaml
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
parser.add_argument(
    "--checks-from",
    type=int,
    help="Will returns checks results from the timestamp passed"
)
parser.add_argument(
    "--checks-to",
    type=int,
    help="Will returns checks results up to the timestamp passed"
)

args = parser.parse_args()
export_type = args.type if args.type else 'all'

try:
    exporter = export.Export(export_type, args.config, args.checks_from, args.checks_to)
    exporter.run()
except yaml.YAMLError as exc:
    print("Unable to read configuration: " + str(exc))
except FileNotFoundError as exc:
    print(exc)
