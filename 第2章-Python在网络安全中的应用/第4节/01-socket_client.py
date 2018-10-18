#!/usr/bin/env python

from socket import *

HOST = '10.211.55.8'
PORT = 9989
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ADDR)

while True:
	data = raw_input(' ~ ')
	if not data:
		break
	tcpClient.send(data)
	data = tcpClient.recv(BUFSIZE)
	if not data:
		break
	print data

tcpClient.close()