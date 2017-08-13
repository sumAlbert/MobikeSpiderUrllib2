# -*- coding: utf-8 -*-
import json
import urllib2
import random
from time import sleep

import MySQLdb
import time
import sys

import thread

DISTX =[]
DISTY =[]
COUNT = 0
def address():
    global DISTX
    global DISTY
    db = MySQLdb.connect(host='localhost',passwd='123aaaaaa',user='root',db='ofo',charset='utf8')
    cursor = db.cursor()
    sql = 'SELECT * FROM putuo_address_info'
    cursor.execute(sql)
    for row in cursor.fetchall():
        DISTX.append(row[1])
        DISTY.append(row[2])
    db.close()

def link(bottom,upper):
    global DISTY
    global DISTX
    global COUNT
    for num in xrange(bottom,upper):
        lon = DISTX[num]
        lat = DISTY[num]
        print COUNT
        spider(lon,lat,10)
        COUNT=COUNT+1
        if COUNT>=5248:
            localtime = time.asctime(time.localtime(time.time()))
            print "本地时间为 :", localtime

def spider(lon,lat,num):
    global COUNT
    url ='http://m5.amap.com/ws/shield/bicycle_status?source=all&language=zh_CN&div=IOSH080102&client_network_class=4&tid=WY6TQ084yVIDAKWNjcm31Ssq&cmd=2&stepid=264&channel=amap7a&appstartid=208705228997&diu2=35F0171F-4627-4183-83AC-EA5092F5DF65&spm=06171318008672&city=021&version=2&session=208705162&cifa=80027004c00d080750f4b101010000000000000000000000000000000000000000000000000000000000000a000000060031302e332e3309006950686f6e65382c3405004150504c450a00382e312e322e32313237000000000000000000001e00&x='+str(lon)+'&y='+str(lat)+'&dip=10920&diu3=3e2a8f227278ca02f2c54d768f8184a449bcbe11&diu=64DA9658-07E5-45EA-AE09-888BB7518A56&aetraffic=9&dic=C3320&dibv=2127&frm=amap&adiu=8eihnid9b799dhhphplfpeb45d2cc6&output=json&sign=0F845F6ED19CC9686D6289AA45DD5DC6&csid=8870CC7B-9D50-499A-8722-19665F20EE33'
    headers = {
        'host':'m5.amap.com',
        'user-agent':'iphone OS 10.3.3',
        'connection': 'close',
        'accept - encoding': 'gzip'
    }
    proxies = [
        # '111.74.233.177:4397',
        # '106.5.249.70:4317',
        # '111.72.113.162:4397',
        # '111.72.165.194:4317',
        '111.74.233.21:4397'
    ]
    # random_proxy = random.choice(proxies)
    # proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    # opener = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(opener)
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request,timeout=60)
        info = html.read()
        print info
        info = json.loads(info)
        bicycle = info['bicycle']
        message = bicycle['message']
        if message=='ok':
            bicycles = bicycle['bicycles']
            items = bicycles['item']
            items_size = len(items)
            if (items_size != 0):
                db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
                cursor = db.cursor()
                sql = "insert into ofo.putuo_valid2 (distX,distY,num,save_time) values (%s,%s,%s,%s) on duplicate key update num = %s"
                param = (lon, lat, str(items_size), '2017-08-13 11:00:00', str(items_size))
                cursor.execute(sql, param)
                db.commit()
                db.close()
                pass
            for item in items:
                db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
                cursor = db.cursor()
                sql = "insert into putuo_mobike_address2 (distX,distY,bikeIds,source,save_time) values (%s,%s,%s,%s,'2017-08-13 11:00:00') on duplicate key update distY = %s"
                param = (str(item['x']), str(item['y']),str(item['id']),str(item['source']),str(item['y']))
                cursor.execute(sql, param)
                db.commit()
                db.close()
    except Exception as ex:
        print ex.message
        if(num>0):
            print ("again")
            num=num-1
            spider(lon,lat,num)
    pass

if __name__ == '__main__':
    localtime = time.asctime(time.localtime(time.time()))
    print "本地时间为 :", localtime
    address()
    try:
        # thread.start_new_thread(link, (0, 50))
        # thread.start_new_thread(link, (50, 100))
        # thread.start_new_thread(link, (100, 150))
        # thread.start_new_thread(link, (150, 200))
        # thread.start_new_thread(link, (200, 250))
        # thread.start_new_thread(link, (250, 300))
        # thread.start_new_thread(link, (300, 350))
        # thread.start_new_thread(link, (350, 400))
        # thread.start_new_thread(link, (400, 450))
        # thread.start_new_thread(link, (450, 500))
        # thread.start_new_thread(link, (500, 550))
        # thread.start_new_thread(link, (550, 600))
        # thread.start_new_thread(link, (600, 650))
        # thread.start_new_thread(link, (650, 700))
        # thread.start_new_thread(link, (700, 750))
        # thread.start_new_thread(link, (750, 800))
        # thread.start_new_thread(link, (800, 850))
        # thread.start_new_thread(link, (850, 900))
        # thread.start_new_thread(link, (900, 950))
        # thread.start_new_thread(link, (950, 1000))
        # thread.start_new_thread(link, (1000, 1050))
        # thread.start_new_thread(link, (1050, 1100))
        # thread.start_new_thread(link, (1100, 1150))
        # thread.start_new_thread(link, (1150, 1200))
        # thread.start_new_thread(link, (1200, 1250))
        # thread.start_new_thread(link, (1250, 1300))
        # thread.start_new_thread(link, (1300, 1350))
        # thread.start_new_thread(link, (1350, 1400))
        # thread.start_new_thread(link, (1400, 1450))
        # thread.start_new_thread(link, (1450, 1500))
        # thread.start_new_thread(link, (1500, 1550))
        # thread.start_new_thread(link, (1550, 1600))
        # thread.start_new_thread(link, (1600, 1650))
        # thread.start_new_thread(link, (1650, 1700))
        # thread.start_new_thread(link, (1700, 1750))
        # thread.start_new_thread(link, (1750, 1800))
        # thread.start_new_thread(link, (1800, 1850))
        # thread.start_new_thread(link, (1850, 1900))
        # thread.start_new_thread(link, (1900, 1950))
        # thread.start_new_thread(link, (1950, 2000))
        # thread.start_new_thread(link, (2000, 2050))
        # thread.start_new_thread(link, (2050, 2100))
        # thread.start_new_thread(link, (2100, 2150))
        # thread.start_new_thread(link, (2150, 2200))
        # thread.start_new_thread(link, (2200, 2250))
        # thread.start_new_thread(link, (2250, 2300))
        # thread.start_new_thread(link, (2300, 2350))
        # thread.start_new_thread(link, (2350, 2400))
        # thread.start_new_thread(link, (2400, 2450))
        # thread.start_new_thread(link, (2450, 2500))
        # thread.start_new_thread(link, (2500, 2550))
        # thread.start_new_thread(link, (2550, 2600))
        # thread.start_new_thread(link, (2600, 2650))
        # thread.start_new_thread(link, (2650, 2700))
        # thread.start_new_thread(link, (2700, 2750))
        # thread.start_new_thread(link, (2750, 2800))
        # thread.start_new_thread(link, (2800, 2850))
        # thread.start_new_thread(link, (2850, 2900))
        # thread.start_new_thread(link, (2900, 2950))
        # thread.start_new_thread(link, (2950, 3000))
        # thread.start_new_thread(link, (3000, 3050))
        # thread.start_new_thread(link, (3050, 3100))
        # thread.start_new_thread(link, (3100, 3150))
        # thread.start_new_thread(link, (3150, 3200))
        # thread.start_new_thread(link, (3200, 3250))
        # thread.start_new_thread(link, (3250, 3300))
        # thread.start_new_thread(link, (3300, 3350))
        # thread.start_new_thread(link, (3350, 3400))
        # thread.start_new_thread(link, (3400, 3450))
        # thread.start_new_thread(link, (3450, 3500))
        # thread.start_new_thread(link, (3500, 3550))
        # thread.start_new_thread(link, (3550, 3600))
        # thread.start_new_thread(link, (3600, 3650))
        # thread.start_new_thread(link, (3650, 3700))
        # thread.start_new_thread(link, (3700, 3750))
        # thread.start_new_thread(link, (3750, 3800))
        # thread.start_new_thread(link, (3800, 3850))
        # thread.start_new_thread(link, (3850, 3900))
        # thread.start_new_thread(link, (3900, 3950))
        # thread.start_new_thread(link, (3950, 4000))
        thread.start_new_thread(link, (4000, 4050))
        thread.start_new_thread(link, (4050, 4100))
        thread.start_new_thread(link, (4100, 4150))
        thread.start_new_thread(link, (4150, 4200))
        thread.start_new_thread(link, (4200, 4250))
        thread.start_new_thread(link, (4250, 4300))
        thread.start_new_thread(link, (4300, 4350))
        thread.start_new_thread(link, (4350, 4400))
        thread.start_new_thread(link, (4400, 4450))
        thread.start_new_thread(link, (4450, 4500))
        thread.start_new_thread(link, (4500, 4550))
        thread.start_new_thread(link, (4550, 4600))
        thread.start_new_thread(link, (4600, 4650))
        thread.start_new_thread(link, (4650, 4700))
        thread.start_new_thread(link, (4700, 4750))
        thread.start_new_thread(link, (4750, 4800))
        thread.start_new_thread(link, (4800, 4850))
        thread.start_new_thread(link, (4850, 4900))
        thread.start_new_thread(link, (4900, 4950))
        thread.start_new_thread(link, (4950, 5000))
        thread.start_new_thread(link, (5000, 5050))
        thread.start_new_thread(link, (5050, 5100))
        thread.start_new_thread(link, (5100, 5150))
        thread.start_new_thread(link, (5150, 5200))
        thread.start_new_thread(link, (5200, 5240))
        while 1:
            pass
    except:
        print "Error: unable to start thread"