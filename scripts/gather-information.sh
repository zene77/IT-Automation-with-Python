#!/bin/bash

echo "Gathering system information..."
echo "Date: $(date)"
echo "-----------------------------------"

echo "System info:"
uname -a
echo "-----------------------------------"

echo "Disk usage:"
df -h
echo "-----------------------------------"

echo "Memory usage:"
free -h
echo "-----------------------------------"

echo "Done."
