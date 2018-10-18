#!/bin/bash

#nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 61.178.98.1/24 -oX /Users/ado/Documents/project-python/url/nmap.xml

if [ $# -lt 1 ]; then
	echo "Example: $0 192.168.1.1/24"
    exit 1
fi
nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml $1

./web_c_scan.py