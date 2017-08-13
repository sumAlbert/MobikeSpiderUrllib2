# -*- coding: gbk -*-
import json
import sys
import gzip
import StringIO
import urllib2

def link():
    info = ""
    try:
        proxy = urllib2.ProxyHandler({'http':'183.45.88.6:9797'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        # ip.filefab.com / index.php
        url = "http://www.ip138.com/"
        headers = {
            'charset': "utf-8",
            'content-type': "application/x-www-form-urlencoded",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            'connection': "Keep-Alive",
            'cache-control': "max-age=0"
        }
        print url
        print ("start")
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request,timeout=30)
        with open('./baidu.txt','w') as fp:
            fp.write(response.read())
        print ("end")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    link()