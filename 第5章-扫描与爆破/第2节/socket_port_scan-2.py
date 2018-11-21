#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from Queue import Queue

# pip install gevent
import gevent
from gevent import monkey; monkey.patch_all()

def scan(ip,queue):
	while not queue.empty():
		port = queue.get_nowait()
		# print ip,port
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		res = s.connect_ex((ip,port))
		if not res:
			print '[*]IP:{}\t{} open!'.format(ip, port)

def main(ip):
	queue = Queue()
	thread_count = 100

	for i in range(1,65535):
		queue.put(i)


	gevent_pool = []
	for i in range(thread_count):
		gevent_pool.append(gevent.spawn(scan,ip,queue))
	gevent.joinall(gevent_pool)

ip = '127.0.0.1'
main(ip)

