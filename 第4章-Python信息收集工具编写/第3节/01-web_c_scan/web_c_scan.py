#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from Queue import Queue
import time
import threading
from IPy import IP
import sys
import re

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",}

class DirScan(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get()
			# print url

			try:
				r = requests.get(url=url, timeout=6, headers=HEADERS)
				# print r.status_code,url
				if r.status_code == 200:
					print '[*]Web Service Found! %s'%url
					try:
						title = re.findall('<title>(.*?)</title>', r.text)[0]
					except:
						title = 'None'

					print url+':'+title
					f = open('result.html','a+')
					f.write('<a href="'+url+'" target="_blank">'+url+'</a>'+'\t\t'+title+'\n')
					f.write('<br>')
					f.close()

			except Exception,e:
				print e
				pass

def create(ips):
	queue = Queue()
	# ip = IP(ips, make_net=True)
	# ip = ips

	req_m = ['http://',]

	ports = ['80','3443']

	dirs = ['','/phpmyadmin',]

	for h in req_m:
		for i in ips:
			for j in ports:
				for k in dirs:
					queue.put(str(h)+str(i)+':'+str(j)+str(k))
	return queue

def main(ips):

	f = open('result.html','w')
	f.close()

	queue = create(ips)
	threads = []

	thread_count = 10
	for i in range(thread_count):
		threads.append(DirScan(queue))

	for t in threads:
		t.start()
	for t in threads:
		t.join()


if __name__ == '__main__':

	with open('nmap.xml') as f:

		ips = re.findall('<address addr="(.*?)" addrtype=', f.read())

		main(ips)
