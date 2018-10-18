#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
import MySQLdb



def proxy_spider():
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}

	url = 'http://www.xicidaili.com/nn'
	r = requests.get(url=url,headers=headers)

	soup = bs(r.content,'lxml')

	datas = soup.find_all(name='tr',attrs={'class':re.compile('|[^odd]')})

	for data in datas:
		soup_proxy_content = bs(str(data),'lxml')
		soup_proxys = soup_proxy_content.find_all(name='td')
		ip = str(soup_proxys[1].string)
		port = str(soup_proxys[2].string)
		types = str(soup_proxys[5].string)
		# for i in [1,2,5]:
		# 	print soup_proxys[i].string
		proxy_check(ip,port,types)
		

def proxy_check(ip,port,types):
	proxy = {}
	proxy[types.lower()] = '%s:%s'%(ip,port)

	# print proxy
	# proxy = {'http': '119.254.84.90:80'}
	try:
		r = requests.get('http://1212.ip138.com/ic.asp', proxies=proxy, timeout=6)
		ip_content = re.findall(r'\[(.*?)\]', r.text)[0]
		if ip == ip_content:
			print proxy
	except Exception,e:
		# print e
		pass




if __name__ == '__main__':
	proxy_spider()