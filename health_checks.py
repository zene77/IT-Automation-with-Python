#!/usr/bin/env python3
import os
import shutil
import sys
import socket
import psutil

def check_reboot():
    """Returns True if the computer has a pending reboot, False otherwise."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """
    Returns True if there isn't at least `min_gb` free OR the free percent
    is below `min_percent`. Otherwise returns False.
    """
    du = shutil.disk_usage(disk)
    # Calculate free in GB and percent free
    free_gb = du.free / 1024**3
    percent_free = 100.0 * du.free / du.total
    if free_gb < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 75

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise."""
    try:
        # Intentional: try resolving a well-known host
        socket.gethostbyname("www.google.com")
        return False
    except Exception:
        return True

def main():
    checks = [
        (check_reboot, "Pending Reboot."),
        (check_root_full, "Root partition full"),
        (check_cpu_constrained, "CPU load too high."),
        (check_no_network, "No working network."),
    ]

    everything_ok = True
    for check, msg in checks:
        try:
            if check():
                print(msg)
                everything_ok = False
        except Exception as e:
            print(f"Error running {check.__name__}: {e}")
            everything_ok = False

    if everything_ok:
        print("Everything ok.")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())

