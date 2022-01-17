#!/usr/bin/python3
"""
Script to convert events to CSV.

This script reads from stdin an event list, as provided by the
papi/net/event/list.json, and produces it on stdout formatted in CSV
format.

:Copyright:
     Copyright 2022 VMware, Inc.  All Rights Reserved.
"""
import csv
import json
import os
import sys


def do_main():
    data = json.load(sys.stdin)

    if not data["data"]:
        return 0

    fieldnames = set()
    for el in data["data"]:
        fieldnames |= set(el.keys())
    writer = csv.DictWriter(sys.stdout, fieldnames=sorted(fieldnames))
    writer.writeheader()
    writer.writerows(data["data"])

    return 0


def main():
    try:
        return do_main()
    except KeyboardInterrupt:
        return 0
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)  
        os.dup2(devnull, sys.stdout.fileno())
        return 0


if __name__ == "__main__":
    sys.exit(main())
