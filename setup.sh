#!/bin/bash

echo Marking iptrace.py as executable...
chmod +x iptrace.py

echo Creating symlink
ln -s iptrace.py /sbin/iptrace

echo Everything\'s set up! Run iptrace to get started.