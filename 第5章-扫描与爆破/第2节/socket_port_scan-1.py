#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def scan(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	res = s.connect_ex((ip,port))
	if not res:
		print '[*]IP:{}\t{} open!'.format(ip, port)

ip = '127.0.0.1'

for i in range(1,65535):
	scan(ip, i)