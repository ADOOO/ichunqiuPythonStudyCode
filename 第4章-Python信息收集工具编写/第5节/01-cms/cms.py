#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtwith
from data import cms_dict
import urlparse

import requests
from config import *
import hashlib
import re
import argparse


class BuiltCms(object):
	"""docstring for BuiltCms"""
	def __init__(self, url):
		super(BuiltCms, self).__init__()
		self.url = url
		
	def run(self):
		#调用builtwith，识别web开发信息
		result = self.built()

		#调用识别方法，识别web的cms信息
		cms = self.cms()
		if cms:
			result[u'cms'] = [u'{}'.format(cms)]
		#打印结果
		return result

	def built(self):
		result = builtwith.parse(self.url)
		if result:
			return result
		else:
			return {}

	def cms(self):
		for cms_name in cms_dict:
			for i in cms_dict[cms_name]:
				url = urlparse.urljoin(self.url, i[0])
				for (methon,content) in i[1].items():
					if methon == 'MD5':
						#进行页面 MD5 识别
						res = requests.get(url=url, headers=headers, timeout=timeout, allow_redirects=allow_redirects, verify=allow_ssl_verify)
						if res.status_code == 200:
							md5 = self.md5(res.content)
							if md5 == content:
								return cms_name
					if methon == 'regex':
						#进行页面 内容匹配 识别
						res = requests.get(url=url, headers=headers, timeout=timeout, allow_redirects=allow_redirects, verify=allow_ssl_verify)
						if res.status_code == 200:
							res_content = self.cont(content, res.content)
							if res_content:
								return cms_name


	def md5(self, content):
		return hashlib.md5(content).hexdigest()

	def cont(self, regex, content):
		if re.search(regex, content):
			return True
		return False

# cms = BuiltCms('http://www.phpcms.cn')
# cms.run()


if __name__ == '__main__':
	paraser = argparse.ArgumentParser(description="CMS BuiltScan Ver:1.0")
	paraser.add_argument("-u", "--url", metavar="", help="weburl addrass")
	args = paraser.parse_args()

	try:
		url = args.url
		if not url:
			print 'Usage : cms.py -u http://test.com/'
			sys.exit(1)
		cms = BuiltCms(url)
		print '[*]Fecting CMS ...'
		result = cms.run()
		print '\n\t{}\n'.format(result)
		print '[-]Complete.'
	except KeyboardInterrupt:
		sys.exit(1)

