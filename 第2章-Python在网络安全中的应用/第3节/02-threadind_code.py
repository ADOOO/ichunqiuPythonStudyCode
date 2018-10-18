#coding=utf-8

import threading
import Queue
from subprocess import Popen,PIPE
import sys

class DoRun(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			ip = self._queue.get()
			#print ip
			check_ping = Popen(['/bin/bash','-c','ping -c 2 '+ip],stdin=PIPE,stdout=PIPE)
			data = check_ping.stdout.read()
			if 'ttl' in data:
				sys.stdout.write(ip+' is UP\n') 


def main():
	threads = []
	threads_count = 100
	queue = Queue.Queue()


	for i in range(1,255):
		queue.put('106.42.25.'+str(i))

	for i in range(threads_count):
		threads.append(DoRun(queue))

	for i in threads:
		i.start()
	for i in threads:
		i.join()
if __name__ == '__main__':
	main()

