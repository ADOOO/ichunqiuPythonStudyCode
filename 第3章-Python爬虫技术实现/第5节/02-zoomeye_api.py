#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


def login():
	url_login = 'https://api.zoomeye.org/user/login'
	data = {
			"username": "adoadmin@163.com",
			"password": "2chunqiu>ado"
			}
	data  = json.dumps(data)

	r = requests.post(url=url_login,data=data)


	return json.loads(r.content)['access_token']

def main():
	url = 'https://api.zoomeye.org/host/search?query=zabbix'
	headers = {'Authorization':'JWT '+login()}
	r = requests.get(url=url,headers=headers)
	# print r.status_code
	# print r.content
	datas = json.loads(r.content)['matches']
	for data in datas:
		print data['ip']

if __name__ == '__main__':
	main()