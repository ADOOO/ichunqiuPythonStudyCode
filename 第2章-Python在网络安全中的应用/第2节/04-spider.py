#coding=utf-8

import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex02/'

headers = {
	'Cookie': 'Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1466473095,1466473149; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1466479519; csrftoken=zWoFvGmSgZr9T2QB9DJvAu3sxmUXL1b5; sessionid=irwdd9xocxm1fu04q2mvro0h8rbjqpur',
}

def run(url_s):
	for i in range(31):
		post_data = {'csrfmiddlewaretoken':'zWoFvGmSgZr9T2QB9DJvAu3sxmUXL1b5','username':'ichunqiu','password':i}
		r = requests.post(url_s,data=post_data,headers=headers)
		if len(r.text) != 2663:
			print r.text
			print i
run(url)
