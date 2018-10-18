#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#.@Filename:.ilink.py
#.@Author..:ADO
'''

from common import http_requests_post, is_domain
import re

class Ilink(object):
    def __init__(self, domain):
        self.domain = domain
        self.site = 'http://i.links.cn/subdomain/'
        self.result = []
    def run(self):
        payload = {
            'domain': self.domain,
            'b2': 1,
            'b3': 1,
            'b4': 1,
        }
        try:
            r = http_requests_post(self.site, payload)
            results = re.findall('value="http://(.*?)"><input', r.text)
            for result in results:
                if is_domain(result):
                    self.result.append(result)
            return list(set(self.result))
        except Exception,e:
            return self.result