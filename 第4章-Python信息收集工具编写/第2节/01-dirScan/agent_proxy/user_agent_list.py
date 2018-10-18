#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_user_agent():
	user_agent_list=[
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML}, like Gecko) Chrome/22.0.1207.1 Safari/537.1'},
					{'User-Agent':'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML}, like Gecko) Chrome/20.0.1132.57 Safari/536.11'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML}, like Gecko) Chrome/20.0.1092.0 Safari/536.6'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML}, like Gecko) Chrome/20.0.1090.0 Safari/536.6'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML}, like Gecko) Chrome/19.77.34.5 Safari/537.1'},
					{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML}, like Gecko) Chrome/19.0.1084.9 Safari/536.5'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML}, like Gecko) Chrome/19.0.1084.36 Safari/536.5'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1063.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1063.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1063.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1062.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1062.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1061.1 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1061.1 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1061.1 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML}, like Gecko) Chrome/19.0.1061.0 Safari/536.3'},
					{'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML}, like Gecko) Chrome/19.0.1055.1 Safari/535.24'},
					{'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML}, like Gecko) Chrome/19.0.1055.1 Safari/535.24'},
					{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'},
					{'User-Agent':'Opera/9.25 (Windows NT 5.1; U; en)'},
					{'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
					{'User-Agent':'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'},
					{'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'},
					{'User-Agent':'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'}
	]

	return random.choice(user_agent_list)


# print random_user_agent()