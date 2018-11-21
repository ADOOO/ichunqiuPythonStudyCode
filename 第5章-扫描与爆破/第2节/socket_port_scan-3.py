#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

from Queue import Queue
import gevent
from gevent import monkey; monkey.patch_all()

# pip install IPy
from IPy import IP

import sys

ports = [21,22,23,25,80,81,82,83,84,85,86,87,88,89,89,110,143,443,513,873,1080,1433,1521,1158,3306,3307,3308,3389,3690,5900,6379,7001,8000,8001,8001,8008,8080,8081,8088,8090,9000,9418,27017,27017,27019,50060]

def portScan(tasks):
	while not tasks.empty():
		task = tasks.get()
		# print task
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		res = s.connect_ex((str(task[0]),int(task[1])))
		if not res:
			print '[*]IP:{}\tPort:{} open!'.format(str(task[0]),int(task[1]))

def ips(target):
	return IP(target)


def main(target):

	tasks = Queue()
	targets = ips(target)
	for ip in targets:
		for port in ports:
			tasks.put((ip,port))

	gevent_pool = []
	for i in range(1000):
		gevent_pool.append(gevent.spawn(portScan,tasks))
	gevent.joinall(gevent_pool)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			main(sys.argv[1])
			sys.exit(0)
		except KeyboardInterrupt:
			print '[*]User exit!'
			sys.exit(0)
		except Exception,e:
			print e.__doc__
			pass
	else:
		print 'Usage: %s 192.168.1.0/24'%sys.argv[0]
		sys.exit(-1)
