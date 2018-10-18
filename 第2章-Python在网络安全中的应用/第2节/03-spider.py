#coding=utf-8

import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex01/'

def run(url_s):
	for i in range(30):
		post_data = {'username':'ichunqiu','password':i}
		r = requests.post(url_s,data=post_data)
		if len(r.text) != 2603:
			print r.text
			print i
run(url)
