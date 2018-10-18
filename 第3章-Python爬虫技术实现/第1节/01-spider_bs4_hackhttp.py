#!/usr/bin/env python
#coding=utf-8

import hackhttp
from bs4 import BeautifulSoup as BS
import re


def tomcat(raw):
	url = 'http://www.cnvd.org.cn/flaw/list.htm?flag=true'
	hh = hackhttp.hackhttp()
	code, head, html, redirect, log = hh.http(url=url,raw=raw)
	soup = BS(html,'lxml')
	tomcat_html = soup.tbody
	#print tomcat_html
	tomcat_cnvds = BS(str(tomcat_html),'lxml')
	cnvds = tomcat_cnvds.find_all(name='a',attrs={'href':re.compile('/flaw/show/CNVD-.*?')})
	#print cnvds
	for cnvd in cnvds:
		print cnvd['title']

raw_start = '''
POST /flaw/list.htm?flag=true HTTP/1.1
Host: www.cnvd.org.cn
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://www.cnvd.org.cn/flaw/list.htm?flag=true
Cookie: __jsluid=00dc737e80eb1e5680a11aad3ff92d45; bdshare_firstime=1472649092629; __jsl_clearance=1472655533.799|0|%2FD0IHtn1rQyGJs1YXvP4%2BM7eKrk%3D; JSESSIONID=61B49CD3B65A2D6BB33F7EAD952D91ED
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 417

number=%E8%AF%B7%E8%BE%93%E5%85%A5%E7%B2%BE%E7%A1%AE%E7%BC%96%E5%8F%B7&startDate=&endDate=&manufacturerId=-1&threadIdStr=&causeIdStr=&referenceScope=-1&order=&baseinfoBeanbeginTime=&max=20&baseinfoBeanFlag=0&condition=1&keyword=tomcat&categoryId=-1&keywordFlag=0&refenceInfo=&cnvdId=&field=&cnvdIdFlag=0&flag=%5BLjava.lang.String%3B%4031de7a6d&serverityIdStr=&editionId=-1&baseinfoBeanendTime=&positionIdStr=&offset='''

for pages_count in range(0,121,20):
	raw = raw_start+str(pages_count)
	tomcat(raw)