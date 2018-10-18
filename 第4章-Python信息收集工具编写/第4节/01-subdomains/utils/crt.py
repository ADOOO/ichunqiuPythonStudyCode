#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#.@Filename:.crt.py
#.@Author..:ADO
'''

from common import http_requests_get, is_domain
import re

class Crt(object):
    def __init__(self, domain):
        self.domain = domain
        self.site = 'https://crt.sh/?q=%25.'
        self.result = []
    def run(self):
        url = self.site + self.domain
        try:
            r = http_requests_get(url=url)
            results = re.findall('</TD>\n    <TD>(.*?)</TD>\n    <TD><A', r.text, re.S)
            for result in results:
                if is_domain(result):
                    self.result.append(result)
            return list(set(self.result))
        except Exception,e:
            return self.result