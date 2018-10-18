#coding=utf-8

import requests
import json
import MySQLdb

url = 'http://www.ichunqiu.com/courses/ajaxCourses'
data_orig = 'courseTag=&courseDiffcuty=&IsExp=&producerId=&orderField=&orderDirection=&tagType=2&pageIndex='

def lesson(data_load):
	headers = {	
			'Host': 'www.ichunqiu.com',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
			'Accept': '*/*',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding': 'gzip, deflate',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'http://www.ichunqiu.com/courses',
			}
	r = requests.post(url=url,headers=headers,data=data_load)
	
	data = json.loads(r.content)

	name_long = len(data['course']['result'])

	for i in range(name_long):
		print data['course']['result'][i]['courseName'],data['course']['result'][i]['producerName'],data['course']['result'][i]['averageScore'],data['course']['result'][i]['presentPrice']
		sql = "insert into lessons (lesson_name,lesson_own,lesson_sorce,lesson_price) values ('%s','%s','%s','%s')"%(data['course']['result'][i]['courseName'].encode('utf-8'),data['course']['result'][i]['producerName'].encode('utf-8'),data['course']['result'][i]['averageScore'].encode('utf-8'),data['course']['result'][i]['presentPrice'].encode('utf-8'))
		cus.execute(sql)


conn = MySQLdb.connect(host = '10.211.55.9',port = 3306,user = 'ichunqiu',passwd = '123#@!',db = 'ichunqiu',charset='utf8')
cus = conn.cursor()

for i in range(1,10):
	data_load = data_orig+str(i)
	lesson(data_load)
cus = conn.commit()
cus.close()
conn.close()



