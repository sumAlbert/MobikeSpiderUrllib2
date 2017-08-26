# -*- coding: utf-8 -*-
# 0.001
import json
import random
import threading
import traceback
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
    sql = 'SELECT * FROM putuo_upper_border_view'
    cursor.execute(sql)
    for row in cursor.fetchall():
        UPPER_X.append(row[0])
        UPPER_Y.append(row[1])
    sql = 'SELECT * FROM putuo_bottom_border_view'
    cursor.execute(sql)
    for row in cursor.fetchall():
        BOTTOM_X.append(row[0])
        BOTTOM_Y.append(row[1])
    interval = Decimal(0.0002)
    for single_lng in xrange(0,len(BOTTOM_X)):
        bottom_lat=BOTTOM_Y[single_lng]
        upper_lat=UPPER_Y[single_lng]
        for i in xrange(0,5):
            cursorx=BOTTOM_X[single_lng]+interval*i
            cursory=bottom_lat
            while cursory<=upper_lat:
                DISTX.append(cursorx.quantize(Decimal('0.000000')))
                DISTY.append(cursory.quantize(Decimal('0.000000')))
                cursory=cursory+interval
        pass
    db.close()

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
    url ='http://m5.amap.com/ws/shield/bicycle_status?source=all&language=zh_CN&div=IOSH080102&client_network_class=4&tid=WY6TQ084yVIDAKWNjcm31Ssq&cmd=2&stepid=264&channel=amap7a&appstartid=208705228997&diu2=35F0171F-4627-4183-83AC-EA5092F5DF65&spm=06171318008672&city=021&version=2&session=208705162&cifa=80027004c00d080750f4b101010000000000000000000000000000000000000000000000000000000000000a000000060031302e332e3309006950686f6e65382c3405004150504c450a00382e312e322e32313237000000000000000000001e00&x='+str(lon)+'&y='+str(lat)+'&dip=10920&diu3=3e2a8f227278ca02f2c54d768f8184a449bcbe11&diu=64DA9658-07E5-45EA-AE09-888BB7518A56&aetraffic=9&dic=C3320&dibv=2127&frm=amap&adiu=8eihnid9b799dhhphplfpeb45d2cc6&output=json&sign=0F845F6ED19CC9686D6289AA45DD5DC6&csid=8870CC7B-9D50-499A-8722-19665F20EE33'
    headers = {
        'host':'m5.amap.com',
        'user-agent':'iphone OS 10.3.3',
        'connection': 'close',
        'accept - encoding': 'gzip'
    }
    random_proxy = random.choice(proxies)
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    request = urllib2.Request(url, headers=headers)
    try:
        html=opener.open(request,timeout=2)
        info=html.read()
        info_out=info
        info=json.loads(info)
        bicycle = info['bicycle']
        message = bicycle['message']
        if message=='ok':
            bicycles = bicycle['bicycles']
            items = bicycles['item']
            threading_lock.acquire()
            COUNT = COUNT + 1
            print COUNT
            threading_lock.release()
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            for item in items:
                cursor = db.cursor()
                sql = "insert into putuo_mobike_address4 (distX,distY,bikeIds,source,save_time,flag) values (%s,%s,%s,%s,%s,'170826_2') on duplicate key update distY = %s"
                param = (str(item['x']), str(item['y']),str(item['id']),str(item['source']),str(SAVE_TIME),str(item['y']))
                cursor.execute(sql, param)
                db.commit()
            db.close()
    except Exception as ex:
        print ("again")
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
    request=urllib2.Request(url,headers=headers)
    proxy_text=urllib2.urlopen(request)
    proxies_temp=proxy_text.read().split('|')
    for proxy in proxies:
        proxies_temp.append(proxy)
    proxies=proxies_temp

if __name__ == '__main__':
    address()
    print ("import address successfully. Now start spider... ")
    threads_1=[]
    try:
        SAVE_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        COUNT=0
        getProxy()
        for threadCount in xrange(0,71):
            start_thread=threadCount*2000
            for num in xrange(0,40):
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
            print len(proxies)
            print ("Now sleep 5s...")
            time.sleep(2)
            getProxy()
        localtime = time.asctime(time.localtime(time.time()))
        print "本地时间为 :", localtime
    except Exception as ex:
        print ex.message