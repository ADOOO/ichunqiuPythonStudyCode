#!/usr/bin/env python

import MySQLdb

#10.211.55.9 3306 ichunqiu 123#@!

conn = MySQLdb.connect(
					host = '10.211.55.9',
					port = 3306,
					user = 'ichunqiu',
					passwd = '123#@!',
	)

cus = conn.cursor()

sql = 'select version()'

cus.execute(sql)

print cus.fetchone()

cus.close()
conn.close()