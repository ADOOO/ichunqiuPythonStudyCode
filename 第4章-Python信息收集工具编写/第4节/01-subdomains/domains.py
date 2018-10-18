#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#.@Filename:.domains.py
#.@Author..:ADO
'''

from utils.crt import Crt
from utils.ilink import Ilink
from utils.brutedns import BruteDns
import argparse
import sys

from common import save_result, read_json

import os


def run(args):

    domain = args.domain
    if not domain:
        print 'Usage : domains,py -d test.com'
        sys.exit(1)


    outfile = '{0}.log'.format(domain)

    script_path = os.path.dirname(os.path.abspath(__file__))
    _cache_path = os.path.join(script_path, 'result/{0}'.format(domain))
    if not os.path.exists(_cache_path):
        os.makedirs(_cache_path, 0777)


    print '[*]Starting Crt fetch ...'
    result = Crt(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'crt.json')
    save_result(_cache_file, result)
    print '\t[-]Fetch complete | Found {}'.format(len(result))

    print '[*]Starting Ilink fetch ...'
    result = Ilink(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'ilink.json')
    save_result(_cache_file, result)
    print '\t[-]Fetch complete | Found {}'.format(len(result))

    print '[*]Starting Brute ...'
    result = BruteDns(domain=domain).run()
    _cache_file = os.path.join(_cache_path, 'brute.json')
    save_result(_cache_file, result)
    print '\n\t[-]Fetch complete | Found {}'.format(len(result))

    _cache_files = ['crt.json', 'ilink.json', 'brute.json']

    subdomains = []

    for file in _cache_files:
        _cache_file = os.path.join(_cache_path, file)
        json_data = read_json(_cache_file)
        if json_data:
            subdomains.extend(json_data)

    subdomains = list(set(subdomains))

    _result_file = os.path.join(script_path, outfile)
    save_result(_result_file, subdomains)

    print '\n[*]{0} {1} subdomains \n\tsave to {2}'.format(domain, len(subdomains), _result_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Domain Scan Ver:S_1.0")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    args = parser.parse_args()

    try:
        run(args)
    except KeyboardInterrupt:
        sys.exit(1)