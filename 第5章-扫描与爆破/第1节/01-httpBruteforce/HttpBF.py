#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 1. 需要处理的参数，接收的参数是什么：payload1,payload2,...payloadN		rawFile		threadcount
# 2. 需要处理多个payload
# 3. 发起http请求，选用hackhttp
# 4. 保存结果，需要按域名及时间新建文件夹，保存成js，然后还要把result.html搞进去，可以在py中定义好模板，直接写文件


import argparse
import sys
import re
import itertools
import hackhttp
from Queue import Queue
import threading
from templates.resultTemplates import *
import os
import time

class httpBrute(object):
	def __init__(self, args):
		self.args = args
		self.payloads = []
		self.payloadsQueue = Queue()
		self.hh = hackhttp.hackhttp()
		self.result = []

	def parseRaw(self):
		with open(self.args.file) as f:
			self.raw = f.read()
		self.httpHost = re.findall('Host: (.*?)\n', self.raw)[0].rstrip()
		self.httpUrl = re.findall('^\w+ (.*?) ', self.raw)[0]
		self.httpTarget = 'http://{}{}'.format(self.httpHost, self.httpUrl)


	def parsePayloads(self):
		for i in range(self.payloadLenght):
			f = open(self.args.payloads[i], 'r')
			for p in f:
				self.payloads.append(p.rstrip())

	def getOrgRes(self):
		code, head, html, redirect_url, log = self.hh.http(self.httpTarget, raw=self.raw)
		self.orgData = html

	def nowTime(slef):
		return str(time.time())

	def saveResult(self):
		script_path = os.path.dirname(os.path.abspath(__file__))
		result_path = os.path.join(script_path, 'result/{}'.format(self.httpHost.replace(':','-')+'-'+self.nowTime()))
		if not os.path.exists(result_path):
			os.makedirs(result_path, 0777)
		f = open(result_path+'/data.js', 'w')
		f.write('var data = {}'.format(self.result))
		f.close()
		f = open(result_path+'/result.html', 'w')
		f.write(html)
		f.close()

		os.system('open {}'.format(result_path+'/result.html'))

	def run(self):
		self.payloadLenght = len(self.args.payloads)
		self.parsePayloads()
		self.payloads = list(itertools.combinations(self.payloads,self.payloadLenght))
		self.payloads = list(set(self.payloads))
		self.parseRaw()
		self.getOrgRes()

		for p in self.payloads:
			self.payloadsQueue.put(p)

		threads = []

		for i in xrange(self.args.thread):
			threads.append(self.httpBruteRun(self.httpTarget, self.payloadsQueue, self.raw, self.orgData, self.result, self.payloadLenght))
		for t in threads:
			t.start()
		for t in threads:
			t.join()

		self.saveResult()

	class httpBruteRun(threading.Thread):
		def __init__(self, httpTarget, payloadsQueue, raw, orgData, result, payloadLenght):
			threading.Thread.__init__(self)
			self.hh = hackhttp.hackhttp(hackhttp.httpconpool(500))
			self.httpTarget = httpTarget
			self._queue = payloadsQueue
			self.raw = raw
			self.orgData = orgData
			self.results = result
			self.length = payloadLenght

		def parseRaw(self, count, payloads):
			keyWord = 'pybf'+str(count+1)
			self._raw = self._raw.replace(keyWord,payloads[count-1])


		def run(self):
			while not self._queue.empty():
				payloads = self._queue.get_nowait()
				self._raw = self.raw
				for i in range(self.length):
					self.parseRaw(i,payloads)
				try:
					code, head, html, redirect_url, log = self.hh.http(self.httpTarget, raw=self._raw)
					bruteState = "Same" if (self.orgData == html) else "Different"
					print '{:<12}\t{:<12}\t{:<12}\t{:<12}'.format(payloads, code, len(html), bruteState)
					self.saveScan(str(payloads), code, len(html), bruteState)
				except Exception,e:
					print e
					pass

		def saveScan(self, userpwd, code, length, bruteState):
			result = []
			result.append(userpwd)
			result.append(code)
			result.append(length)
			result.append(bruteState)
			self.results.append(result)




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="httpBruteForce Tool Ver:1.0")
	parser.add_argument("-t", "--thread", metavar="", type=int, default=8, help="Thread Count default is 8")
	parser.add_argument("-f", "--file", metavar="", help="rawFile")
	parser.add_argument("-p", "--payloads", nargs='*', help="Payloads")
	args = parser.parse_args()

	if args.file and args.payloads:
		try:
			httpBrute = httpBrute(args)
			httpBrute.run()
		except KeyboardInterrupt:
			sys.exit(-1)
		sys.exit(1)
	parser.print_help()