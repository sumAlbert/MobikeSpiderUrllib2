# -*- coding: utf-8 -*-
# 0.001
import json
import random
import threading
import traceback
import urllib
import urllib2
from decimal import Decimal

import MySQLdb
import time
import thread

SAVE_TIME=''
DISTX =[]
DISTY =[]
UPPER_X =[]
UPPER_Y = []
BOTTOM_X =[]
BOTTOM_Y = []
COUNT = 0
proxies = []
time_lock='false'
stop_lock='false'
threading_lock=threading.Lock()

class MyThread(threading.Thread):
    upper=50
    bottom=0
    def __init__(self, bottom,upper):
        threading.Thread.__init__(self)
        self.upper=upper
        self.bottom=bottom
    def run(self):
        link(bottom=self.bottom,upper=self.upper)
        pass
    def stop(self):
        self.thread_stop = True
def address():
    global DISTX
    global DISTY
    db = MySQLdb.connect(host='localhost',passwd='123aaaaaa',user='root',db='ofo',charset='utf8')
    cursor = db.cursor()
    sql = 'SELECT * FROM lujiazui_upper_border_view'
    cursor.execute(sql)
    for row in cursor.fetchall():
        UPPER_X.append(row[0])
        UPPER_Y.append(row[1])
    sql = 'SELECT * FROM lujiazui_bottom_border_view'
    cursor.execute(sql)
    for row in cursor.fetchall():
        BOTTOM_X.append(row[0])
        BOTTOM_Y.append(row[1])
    interval = Decimal(0.0005)
    for single_lng in xrange(0,len(BOTTOM_X)):
        bottom_lat=BOTTOM_Y[single_lng]
        upper_lat=UPPER_Y[single_lng]
        for i in xrange(0,2):
            cursorx=BOTTOM_X[single_lng]+interval*i
            cursory=bottom_lat
            while cursory<=upper_lat:
                DISTX.append(cursorx.quantize(Decimal('0.000000')))
                DISTY.append(cursory.quantize(Decimal('0.000000')))
                cursory=cursory+interval
        pass
    db.close()
def time_start_lock():
    global time_lock
    time_lock='true'
    time.sleep(1800)
    time_lock='false'
def time_stop_lock():
    global stop_lock
    time.sleep(86600)
    stop_lock='true'
def link(bottom,upper):
    global DISTY
    global DISTX
    global COUNT
    global threading_lock
    for num in xrange(bottom,upper):
        if num<len(DISTX):
            lon = DISTX[num]
            lat = DISTY[num]
            spider(lon,lat,20)
def spider(lon,lat,num):
    global COUNT
    global proxies
    global SAVE_TIME
    url ='https://api.open.ofo.com/v1/near/bicycle'
    headers = {
        'Host': 'api.open.ofo.com',
        'Content - Type': 'application / json',
        'Accept': '* / *',
        'Accept - Encoding': 'gzip, deflate',
        'Connection': 'keep - alive',
        'Pragma': 'no - cache',
        'User - Agent': 'OneTravel/5.1.8 (iPhone; iOS 10.3.3; Scale/2.00)',
        'Accept - Language': 'zh - Hans - CN;q = 1',
        'Cache - Control': 'no - cache'

    }
    values={"appKey":"didi","number":"20","longitude":lon,"radius":"200","mapType":"1","latitude":lat,"datatype":"101","appversion":"5.1.8"}
    data = urllib.urlencode(values)
    random_proxy = random.choice(proxies)
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    request = urllib2.Request(url, headers=headers,data=data)
    try:
        html=opener.open(request,timeout=2)
        info=html.read()
        infoout=info
        info=json.loads(info)
        bicycle = info['body']
        items = bicycle['bicycles']
        threading_lock.acquire()
        COUNT = COUNT + 1
        print COUNT
        # print infoout
        threading_lock.release()
        db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
        for item in items:
            cursor = db.cursor()
            sql = "insert into putuo_mobike_address5 (distX,distY,bikeIds,source,save_time,flag) values (%s,%s,%s,'ofo',%s,'170830_2') on duplicate key update distY = %s"
            param = (str(item['longitude']), str(item['latitude']),str(item['bicycleNo']),str(SAVE_TIME),str(item['latitude']))
            cursor.execute(sql, param)
            db.commit()
        db.close()
    except Exception as ex:
        print ex.message
        traceback.print_exc()
        print "again"
        if(num>0):
            num=num-1
            if len(proxies)>3:
                threading_lock.acquire()
                if proxies.count(random_proxy)>0:
                    proxies.remove(random_proxy)
                threading_lock.release()
            spider(lon,lat,num)

def getProxy():
    global proxies
    url='http://dev.kuaidaili.com/api/getproxy/?orderid=990355466199475&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp1=1&sep=4'
    headers={
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.8',
        'Cache - Control': 'max - age = 0',
        'Connection' :'keep - alive',
        'Host' :'dev.kuaidaili.com',
        'Upgrade - Insecure - Requests':'1',
        'User - Agent':'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 60.0.3112.101 Safari / 537.36'
    }
    try:
        request=urllib2.Request(url,headers=headers)
        proxy_text=urllib2.urlopen(request)
        proxies_temp=proxy_text.read().split('|')
        # for proxy in proxies:
        #     proxies_temp.append(proxy)
        proxies=proxies_temp
        print len(proxies)
    except Exception as ex:
        print ex.message
        traceback.print_exc()

if __name__ == '__main__':
    address()
    print ("import address successfully. Now start spider... ")
    thread.start_new_thread(time_stop_lock, ())
    threads_1=[]
    try:
        COUNT=0
        getProxy()
        while 1:
            SAVE_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            thread.start_new_thread(time_start_lock ,())
            for threadCount in xrange(0,3):
                start_thread=threadCount*3000
                for num in xrange(0,60):
                    start_num=start_thread+num*50
                    stop_num = start_thread+num*50+50
                    myThread = MyThread(start_num,stop_num)
                    threads_1.append(myThread)
                for t in threads_1:
                    t.start()
                for t in threads_1:
                    t.join()
                while len(threads_1) != 0:
                    threads_1.pop()
                print ("number of proxies saved:")
                print ("Now sleep 5s...")
                time.sleep(5)
                getProxy()
            while 1:
                time.sleep(1)
                print (time_lock == 'false')
                if time_lock == 'false':
                    COUNT=0
                    break
            if stop_lock == 'true':
                break
            pass
        localtime = time.asctime(time.localtime(time.time()))
        print "本地时间为 :", localtime
    except Exception as ex:
        print ex.message