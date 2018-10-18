#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import threading
import Queue
from bs4 import BeautifulSoup as bs
import json
import time

'''
pages = https://www.seebug.org/vuldb/vulnerabilities?page=1

vul = https://www.seebug.org/vuldb/ssvid-15334

exchange = https://www.seebug.org/vuldb/exchange/15334 POST {"type":"poc","anonymous":true}

down = https://www.seebug.org/vuldb/downloadPoc/15334


第一步 访问所有的pages 匹配所有的漏洞地址
第二部 模拟兑换操作（不是所有都能成功兑换）
	兑换成功 =52 已经兑换=69  KB不足=75  无法兑换=63
第三步 下载poc
'''

headers = {
			'Host': 'www.seebug.org',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'X-CSRFToken': 'n9VSaOaBVLpOFarY7CjIrEBny1EzKmPS',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'https://www.seebug.org/vuldb/ssvid-15228',
			'Cookie': 'Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1473304470,1473385202,1473646648,1473784502; csrftoken=n9VSaOaBVLpOFarY7CjIrEBny1EzKmPS; __jsluid=5918dffe0fbf0c3b9c8203ad56207659; sessionid=oxf3ln634lfaqz2jvrk3964oppti9i01; messages="39014e51bdb8555377fe6e6e9786951270d18e11$[[\"__json_message\"\0540\05425\054\"Login succeeded. Welcome\054 ADO_ichunqiu.\"]]"',
			'Connection': 'keep-alive',
			}

class SeebugPoc(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get_nowait()
			spider(url)


def spider(url):
	dic = {}
	dic['type'] = 'poc'
	dic['anonymous'] = 'true'
	datas = json.dumps(dic)

	r = requests.get(url=url,headers=headers)
	# print r.status_code
	soup = bs(r.content,'lxml')
	vulids = soup.find_all(name='a',attrs={'class':'vul-title'})
	for vulid in vulids:
		print vulid['href'].split('-')[-1],vulid['title']
		exchange_url = 'https://www.seebug.org/vuldb/exchange/'+vulid['href'].split('-')[-1]
		
		# print exchange_url
		exchange_r = requests.post(url=exchange_url, headers=headers, data=datas)
		print exchange_r.status_code,len(exchange_r.content),exchange_r.content
		if len(exchange_r.content) in [52,69]:

			down_url = 'https://www.seebug.org/vuldb/downloadPoc/'+vulid['href'].split('-')[-1]
			print down_url
			down_r = requests.get(url=down_url,headers=headers)
			f = open('poc/'+vulid['href'].split('-')[-1]+'.py','w')
			f.write(down_r.content)
			f.close
		time.sleep(2)

def main():
	queue = Queue.Queue()
	for i in range(2572,2574):
		queue.put('https://www.seebug.org/vuldb/vulnerabilities?page='+str(i))

	threads = []
	thread_count = 1

	for i in range(thread_count):
		threads.append(SeebugPoc(queue))

	for t in threads:
		t.start()

	for t in threads:
		t.join()

if __name__ == '__main__':
	main()