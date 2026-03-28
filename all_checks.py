#!/usr/bin/env python3

import shutil
import sys
import os

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [
        (check_reboot, "Pending Reboot."),
        (check_root_full, "Root partition full."),
    ]

    everything_ok = True

    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)


