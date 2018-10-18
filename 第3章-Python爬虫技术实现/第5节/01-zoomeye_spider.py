#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

headers = {
			'Host': 'www.zoomeye.org',
			'Connection': 'close',
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Referer': 'https://www.zoomeye.org/',
			'Accept-Encoding': 'gzip, deflate, sdch, br',
			'Accept-Language': 'zh-CN,zh;q=0.8',
			'Cookie': '__jsluid=874dc7bc56e213f046ad494670741232; csrftoken=EhzomPw6KxsEpgfsoKWS8Y7rkLCE1eQB; sessionid=nu1vwwuav6a8sz737s7hw2b06uxl40lz; __jsl_clearance=1481722902.39|0|W1e6IKKpsWjALCmwk5PkuAsnDuY%3D; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1481643963,1481645449,1481646199,1481722905; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1481723390'

			}


url = 'https://www.zoomeye.org/search?t=host&q=tomcat'
def spider(url):
	r = requests.get(url=url,headers=headers)
	soup = bs(r.content,'lxml')
	ips = soup.find_all(name='a',attrs={'class':'ip'})

	ports = soup.find_all(name='i',attrs={'class':None})

	for ip,port in zip(ips,ports):
		print ip.string,port.string.replace('\n','').replace(' ','')

def main():
	for i in range(1,11):
		url = 'https://www.zoomeye.org/search?t=host&q=tomcat&p=10'+str(i)
		spider(url)