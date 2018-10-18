#coding=utf-8

import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page='

headers = {
	'Cookie': 'Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1466473095,1466473149; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1466480788; csrftoken=s66D9xZCf3umDBJrAJH9VCuYBFHaqdOA; sessionid=1f5gt4ya1zdzq2u22z4a7rn83qtsft8b',
}


def run(url_s):
	dic = {}
	for i in range(1,14):
		url = url_s+str(i)
		r = requests.get(url,headers=headers)

		pos = re.findall('password_pos">(.*?)</td>', r.text)
		val = re.findall('password_val">(.*?)</td>', r.text)

		for i in pos:
			for j in val:
				dic[int(i)]=int(j)

	print dic
	print dic.keys()
	print dic.keys()
	key = 'key:'
	for i in dic.values():
		key = key+str(i)
	print key
run(url)
