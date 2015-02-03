#!/usr/bin/env python
# -.- coding: utf-8 -.-

import sys
import os
import re
import requests

import urllib2
from BeautifulSoup import BeautifulSoup

def linkize(fname):
    f = open(fname)
    
    print '===='
    def replace(m):
        if m:
            url = m.group(0)
            print 'request url:', url
            text = requests.get(url).text
            soup = BeautifulSoup(text)
            get_title = soup.title.string
            print '  get title:', get_title
            print '--'                                    
            return '[%s](%s)'.encode('u8') % (get_title.encode('u8'), url)

    ret = re.sub(r'http[s]?://\S+', replace, f.read())

    f.close()
    os.rename(fname, fname+'.bak')
    fout = open(fname, 'w')
    fout.write(ret)
    fout.close()

    
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        linkize(sys.argv[1])
    else:
        print 'usage linkize.py <filename>'
