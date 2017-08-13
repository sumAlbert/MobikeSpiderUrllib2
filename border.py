# -*- coding: utf-8 -*-
import json
import sys
import gzip
import StringIO
import urllib2

def link():
    offset = 0.002
    start = 121.966
    for num in xrange(0,15):
        lng=(start+num*offset)
        with open('./border.txt','a') as fp:
            fp.write("new BMap.Point("+str(lng)+",31.113),\n")

if __name__ == '__main__':
    link()