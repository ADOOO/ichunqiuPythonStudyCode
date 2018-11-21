#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nmap
import argparse
import sys


def scan(args):

	# ip,arguments
	target = args.target
	option = args.option

	nm = nmap.PortScanner()
	nm.scan(hosts=target, arguments=option)

	for host in nm.all_hosts():
		for proto in nm[host].all_protocols():
			lport = nm[host][proto].keys()
			lport.sort()
			for port in lport:
				print ('[*]{}\t{}\t{}'.format(host, port, nm[host][proto][port]['state']))



if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="Port Scan Ver:1.0")
	parser.add_argument("-t", "--target", metavar="" , help="scan target")
	parser.add_argument("-o", "--option", metavar="" , help="scan option", default="")

	args = parser.parse_args()

	if args.target:
		try:
			scan(args)
			sys.exit(1)
		except Exception,e:
			print e.__doc__
			sys.exit(-1)

	parser.print_help()