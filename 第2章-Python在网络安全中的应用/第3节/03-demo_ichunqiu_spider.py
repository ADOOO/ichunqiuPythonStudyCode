#coding=utf-8

import requests
import json

#url = 'http://www.ichunqiu.com/courses/ajaxCourses?courseTag=&pageIndex=1&courseDiffcuty=0&orderField=0&orderDirection=2&producerId='
url_start = 'http://www.ichunqiu.com/courses/ajaxCourses?courseTag=&pageIndex='



def lesson(url):
	headers = {	
			'Host': 'www.ichunqiu.com',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'http://www.ichunqiu.com/courses',
			}

	r = requests.get(url=url,headers=headers)

	data = json.loads(r.text)

	name_long = len(data['result'])

	for i in range(name_long):
		print data['result'][i]['courseName'],data['result'][i]['producerName']

for i in range(1,9):
	url = url_start+str(i)+'&courseDiffcuty=0&orderField=0&orderDirection=2&producerId='
	lesson(url)




