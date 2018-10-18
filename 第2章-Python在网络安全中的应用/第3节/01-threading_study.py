#/usr/bin/python

import threading
import time

def fun1(key):
	print 'Hello %s:%s'%(key,time.ctime())

def main():
	threads = []
	key = 'abcdef'
	thread_count = len(key)
	for i in range(thread_count):
		t = threading.Thread(target=fun1,args=(key[i],))
		threads.append(t)

	for i in range(thread_count):
		threads[i].start()
	for i in range(thread_count):
		threads[i].join()

main()