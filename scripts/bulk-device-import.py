#!/usr/bin/env python3
"""
bulk-device-import.py
Imports devices from a CSV file into Traccar via the REST API.

CSV format (no header row):
  unique_id,name,phone

Example:
  861234567890001,Asset-001,+447700900001
  861234567890002,Asset-002,+447700900002

Usage:
  python bulk-device-import.py --server http://<IP>:8082 --user admin --password PASSWORD --csv devices.csv
"""

import argparse
import csv
import sys
import requests
from requests.auth import HTTPBasicAuth


def import_devices(server, user, password, csv_path):
    auth = HTTPBasicAuth(user, password)
    url = f"{server.rstrip('/')}/api/devices"

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        success, failed = 0, 0

        for row in reader:
            if not row or row[0].startswith("#"):
                continue  # skip blank/comment lines

            unique_id = row[0].strip()
            name = row[1].strip() if len(row) > 1 else unique_id
            phone = row[2].strip() if len(row) > 2 else ""

            payload = {"name": name, "uniqueId": unique_id, "phone": phone}
            resp = requests.post(url, json=payload, auth=auth)

            if resp.status_code in (200, 201):
                print(f"  ✓ {name} ({unique_id})")
                success += 1
            else:
                print(f"  ✗ {name} ({unique_id}) — HTTP {resp.status_code}: {resp.text}")
                failed += 1

    print(f"\nDone: {success} imported, {failed} failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk import devices into Traccar")
    parser.add_argument("--server", required=True, help="Traccar server URL, e.g. http://1.2.3.4:8082")
    parser.add_argument("--user", default="admin")
    parser.add_argument("--password", required=True)
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    args = parser.parse_args()

    import_devices(args.server, args.user, args.password, args.csv)
