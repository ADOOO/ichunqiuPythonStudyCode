#!/usr/bin/env python
#coding=utf-8

import requests
import threading
import time
from Queue import Queue
import re
from bs4 import BeautifulSoup as bs
import urllib



class JindanSpider(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			page_url = self._queue.get_nowait()
			#print page_url
			self.spider(page_url)


	def spider(self,url):
		#url = 'http://jandan.net/ooxx'
		headers = {'User-Agent':'ichunqiu_spider_test ver 1.2'}
		r = requests.get(url=url,headers=headers)
		#img_urls = re.findall('<img src="(.*?)" />', r.content)
		soup = bs(r.content,'lxml')
		img_urls = soup.find_all(name='img',attrs={'border':None})
		for i in img_urls:
			try:
				img_url = i['org_src']
			except:
				img_url = i['src']
			print img_url
			#urllib.urlretrieve(img_url,filename='img/'+img_url.split('/')[-1])



def main():
	queue = Queue()

	for i in range(2120,2133):
		queue.put('http://jandan.net/ooxx/page-'+str(i))

	threads = []
	thread_count = 5

	for i in xrange(thread_count):
		threads.append(JindanSpider(queue))

	for t in threads:
		t.start()

	for t in threads:
		t.join()


if __name__ == '__main__':
	main()




