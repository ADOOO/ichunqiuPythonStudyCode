#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IPy import IP

ips = IP('127.0.0.0/24')

for ip in ips:
	print ip