@echo off
color 0a
title scan

nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml %1%
web_c_scan.py