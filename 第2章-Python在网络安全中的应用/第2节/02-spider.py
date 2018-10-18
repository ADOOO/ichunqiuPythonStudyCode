#coding=utf-8

import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

def run(url_s):
	r = requests.get(url_s)
	num = re.findall('<h3>\D*(\d*)\D*</h3>', r.text)
	#print num
	url_s = url+num[0]
	print url_s
	run(url_s)

run(url)
