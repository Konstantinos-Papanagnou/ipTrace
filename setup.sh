#!/bin/bash

echo Marking iptrace.py as executable...
chmod +x iptrace.py

echo Creating symlink
ln -s $(pwd)/iptrace.py /bin/iptrace

echo Everything\'s set up! Run iptrace to get started.