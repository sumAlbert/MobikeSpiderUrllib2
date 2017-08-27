# -*- coding: utf-8 -*-
import json
import sys
import gzip
import StringIO
import urllib2

import MySQLdb


def link():
    db=MySQLdb.connect(host='localhost',user='root',passwd='123aaaaaa',db='ofo')
    cursor=db.cursor()
    sql='SELECT save_time FROM ofo.putuo_mobike_address4 where flag=\'170827_4\' group by save_time'
    cursor.execute(sql)
    for row in cursor.fetchall():
        print "\""+str(row[0])+"\","

if __name__ == '__main__':
    link()