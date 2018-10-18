#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from Queue import Queue
import threading
from bs4 import BeautifulSoup as bs
import re

# https://www.baidu.com/s?wd=ichunqiu&pn=10
# wd参数控制的是keyword，pn参数控制的是页码，页码从0开始，每页增10，最大页码为750

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}

class BaiduSpider(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get()
			try:
				self.spider(url)
			except Exception,e:
				print e
				pass

	def spider(self,url):
		r = requests.get(url=url,headers=headers)
		soup = bs(r.content,'lxml')
		urls = soup.find_all(name='a',attrs={'data-click':re.compile(('.')),'class':None})
		for url in urls:
			r_get_url = requests.get(url=url['href'],headers=headers,timeout=8)
			if r_get_url.status_code == 200:
				url_para = r_get_url.url
				url_index_tmp = url_para.split('/')
				url_index = url_index_tmp[0]+'//'+url_index_tmp[2]
				print url_para+'\n'+url_index
				f1 = open('out_para.txt','a+')
				f1.write(url_para+'\n')
				f1.close()
				with open('out_index.txt') as f:
					if url_index not in f.read():
						f2 = open('out_index.txt','a+')
						f2.write(url_index+'\n')
						f2.close()

def main(keyword):
	queue = Queue()
	for i in range(0,760,10):
		queue.put('https://www.baidu.com/s?wd=%s&pn=%s'%(keyword,str(i)))

	threads = []
	thread_count = 4

	for i in range(thread_count):
		threads.append(BaiduSpider(queue))
	for t in threads:
		t.start()
	for t in threads:
		t.join()


if __name__ == '__main__':

	f1 = open('out_para.txt','w')
	f1.close()
	f2 = open('out_index.txt','w')
	f2.close()

	if len(sys.argv) != 2:
		print 'Enter:%s keyword'%sys.argv[0]
		sys.exit(-1)
	else:
		main(sys.argv[1])








