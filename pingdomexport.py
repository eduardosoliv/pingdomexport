import json
import requests
import argparse
import sys
from pingdomexport import export

parser = argparse.ArgumentParser()
parser.add_argument(
    "--type",
    type=str,
    help="Export type if only the check list or the results, options: checks|results|all"
)
args = parser.parse_args()

export_type = 'all'
if args.type:
    if args.type in ['checks', 'results', 'all']:
        export_type = args.type
    else:
        print("Invalid export type must be checks|results|all")

export.Export(export_type).run()
