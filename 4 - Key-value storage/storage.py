import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="type key here")
parser.add_argument("--val", default=None, help="type value here")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), "storage.data")

if os.path.exists(storage_path):
    with open(storage_path) as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
else:
    with open(storage_path, 'w') as f:
        data = {}

if args.val:
    data.setdefault(args.key, []).append(args.val)
    with open(storage_path, 'w') as f:
        json.dump(data, f)
else:
    result = ', '.join(data.get(args.key, ''))
    print(result or None)




