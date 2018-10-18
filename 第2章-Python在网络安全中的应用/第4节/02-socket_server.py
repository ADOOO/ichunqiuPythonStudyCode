#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 9990
BUFSIZE = 1024

ADDR = (HOST,PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
	print 'waiting for connection...'
	tcpClient, addr = tcpServer.accept()
	print '...connected from:',addr
	while True:
		data = tcpClient.recv(BUFSIZE)
		if not data:
			break
		if data == 'bye':
			print 'loginout ByeBye'
		print '[%s] %s:%s'%(ctime(),addr,data)
		tcpClient.send('[%s] %s'%(ctime(),data))
	break

tcpClient.close()
tcpServer.close()