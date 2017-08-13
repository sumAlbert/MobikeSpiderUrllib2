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
        lon = DISTX[COUNT]
        lat = DISTY[COUNT]
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
        # '106.5.7.184:4397',
        # '182.101.253.200:4317'
        '124.161.43.134:4399'
    ]
    # random_proxy = random.choice(proxies)
    # proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    # opener = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(opener)
    request = urllib2.Request(url, headers=headers)
    try:
        # html = urllib2.urlopen(request,timeout=60)
        # info = html.read()
        info = '{"bicycle":{"message":"ok","bicycles":{"scope":500,"item":[{"id":"0216714691","distance":1.5641576,"source":"mobike","icon_code":"mobike-1","y":31.230741469450585,"x":121.41094423691203},{"id":"8620995523","distance":1.627437,"source":"mobike","icon_code":"mobike-1","y":31.230730463696993,"x":121.41094823506295},{"id":"Z5leG5","distance":1.7923707,"source":"ofo","icon_code":"ofo-0","y":31.2307415,"x":121.4109471575},{"id":"0216091318","distance":2.8925462,"source":"mobike","icon_code":"mobike-2","y":31.230737464661477,"x":121.4109612327754},{"id":"zmoAv6","distance":2.9657187,"source":"ofo","icon_code":"ofo-0","y":31.2307094906,"x":121.4109161616},{"id":"0216645576","distance":3.0612664,"source":"mobike","icon_code":"mobike-1","y":31.23070545444308,"x":121.410935235772},{"id":"0216084699","distance":3.2005754,"source":"mobike","icon_code":"mobike-2","y":31.230747469436064,"x":121.41096023387061},{"id":"0kwkle","distance":3.2046776,"source":"ofo","icon_code":"ofo-0","y":31.2307455098,"x":121.410901168},{"id":"YAyPPB","distance":4.3048644,"source":"ofo","icon_code":"ofo-0","y":31.2307345073,"x":121.4108861704},{"id":"0216769556","distance":4.9421444,"source":"mobike","icon_code":"mobike-1","y":31.230696445797342,"x":121.41096122920025},{"id":"0216138942","distance":4.979741,"source":"mobike","icon_code":"mobike-2","y":31.23076447586541,"x":121.41096823356564},{"id":"QQvBkg","distance":5.019775,"source":"ofo","icon_code":"ofo-0","y":31.2307094958,"x":121.4108861682},{"id":"4zrGEA","distance":5.2691264,"source":"ofo","icon_code":"ofo-0","y":31.2307665075,"x":121.4109701545},{"id":"0216092741","distance":6.0926547,"source":"mobike","icon_code":"mobike-2","y":31.230777481846076,"x":121.41096823469923},{"id":"0216083489","distance":6.602272,"source":"mobike","icon_code":"mobike-2","y":31.23069244029646,"x":121.41098222415128},{"id":"qG5GGR","distance":6.6250653,"source":"ofo","icon_code":"ofo-0","y":31.2307705067,"x":121.4109851515},{"id":"0216758875","distance":6.7673645,"source":"mobike","icon_code":"mobike-1","y":31.23073247969135,"x":121.41086025461954},{"id":"0216536694","distance":6.9065733,"source":"mobike","icon_code":"mobike-1","y":31.23074946319328,"x":121.41100122484903},{"id":"9g2YDn","distance":6.916279,"source":"ofo","icon_code":"ofo-0","y":31.2307745086,"x":121.4109851519},{"id":"k4VlVW","distance":7.23567,"source":"ofo","icon_code":"ofo-0","y":31.2306804824,"x":121.4108861656},{"id":"WrqanM","distance":7.28392,"source":"ofo","icon_code":"ofo-0","y":31.2307265088,"x":121.4108551764},{"id":"3Mxljw","distance":7.433947,"source":"ofo","icon_code":"ofo-0","y":31.2307995293,"x":121.4109321659},{"id":"0216848704","distance":7.477063,"source":"mobike","icon_code":"mobike-1","y":31.2306964622804,"x":121.41086525039007},{"id":"8621315145","distance":7.602694,"source":"mobike","icon_code":"mobike-1","y":31.230666440457863,"x":121.41091223746074},{"id":"8621205321","distance":7.82365,"source":"mobike","icon_code":"mobike-1","y":31.230800495034096,"x":121.41095324005333},{"id":"omjxvE","distance":7.961743,"source":"ofo","icon_code":"ofo-0","y":31.2307815316,"x":121.410870178},{"id":"0216833512","distance":8.507305,"source":"mobike","icon_code":"mobike-1","y":31.230660429406257,"x":121.41096022628433},{"id":"0216104306","distance":8.933757,"source":"mobike","icon_code":"mobike-2","y":31.230773472300218,"x":121.41101222445947},{"id":"lrlRg1","distance":8.964904,"source":"ofo","icon_code":"ofo-0","y":31.2306564688,"x":121.4109011603},{"id":"1m6NOa","distance":9.461213,"source":"ofo","icon_code":"ofo-0","y":31.2307385182,"x":121.4108321825}],"icon_version":"1500385476"},"code":0}}'
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
                param = (lon, lat, str(items_size), '2011-11-11 11:11:11', str(items_size))
                cursor.execute(sql, param)
                db.commit()
                db.close()
                pass
            for item in items:
                db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
                cursor = db.cursor()
                sql = "insert into putuo_mobike_address2 (distX,distY,bikeIds,source,save_time) values (%s,%s,%s,%s,'2011-11-11 11:11:11') on duplicate key update distY = %s"
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
        else:
            print ("failure")
            COUNT=COUNT+1
            next_lon = DISTX[COUNT]
            next_lat = DISTY[COUNT]
            spider(next_lon, next_lat, 10)
    pass

if __name__ == '__main__':
    address()
    spider(121.417212,31.237027,10)
    # try:
    #     thread.start_new_thread(link, (0, 50))
    #     thread.start_new_thread(link, (50, 100))
    #     thread.start_new_thread(link, (100, 150))
    #     thread.start_new_thread(link, (150, 200))
    #     thread.start_new_thread(link, (200, 250))
    #     thread.start_new_thread(link, (250, 300))
    #     thread.start_new_thread(link, (300, 350))
    #     thread.start_new_thread(link, (350, 400))
    #     thread.start_new_thread(link, (400, 450))
    #     thread.start_new_thread(link, (450, 500))
    #     thread.start_new_thread(link, (500, 550))
    #     thread.start_new_thread(link, (550, 600))
    #     thread.start_new_thread(link, (600, 650))
    #     thread.start_new_thread(link, (650, 700))
    #     thread.start_new_thread(link, (700, 750))
    #     thread.start_new_thread(link, (750, 800))
    #     thread.start_new_thread(link, (800, 850))
    #     thread.start_new_thread(link, (850, 900))
    #     thread.start_new_thread(link, (900, 950))
    #     thread.start_new_thread(link, (950, 1000))
    #     thread.start_new_thread(link, (1000, 1050))
    #     thread.start_new_thread(link, (1050, 1100))
    #     thread.start_new_thread(link, (1100, 1150))
    #     thread.start_new_thread(link, (1150, 1200))
    #     thread.start_new_thread(link, (1200, 1250))
    #     thread.start_new_thread(link, (1250, 1300))
    #     thread.start_new_thread(link, (1300, 1350))
    #     thread.start_new_thread(link, (1350, 1400))
    #     thread.start_new_thread(link, (1400, 1450))
    #     thread.start_new_thread(link, (1450, 1500))
    #     thread.start_new_thread(link, (1500, 1550))
    #     thread.start_new_thread(link, (1550, 1600))
    #     thread.start_new_thread(link, (1600, 1650))
    #     thread.start_new_thread(link, (1650, 1700))
    #     thread.start_new_thread(link, (1700, 1750))
    #     thread.start_new_thread(link, (1750, 1800))
    #     thread.start_new_thread(link, (1800, 1850))
    #     thread.start_new_thread(link, (1850, 1900))
    #     thread.start_new_thread(link, (1900, 1950))
    #     thread.start_new_thread(link, (1950, 2000))
    #     thread.start_new_thread(link, (2000, 2050))
    #     thread.start_new_thread(link, (2050, 2100))
    #     thread.start_new_thread(link, (2100, 2150))
    #     thread.start_new_thread(link, (2150, 2200))
    #     thread.start_new_thread(link, (2200, 2250))
    #     thread.start_new_thread(link, (2250, 2300))
    #     thread.start_new_thread(link, (2300, 2350))
    #     thread.start_new_thread(link, (2350, 2400))
    #     thread.start_new_thread(link, (2400, 2450))
    #     thread.start_new_thread(link, (2450, 2500))
    #     thread.start_new_thread(link, (2500, 2550))
    #     thread.start_new_thread(link, (2550, 2600))
    #     thread.start_new_thread(link, (2600, 2650))
    #     thread.start_new_thread(link, (2650, 2700))
    #     thread.start_new_thread(link, (2700, 2750))
    #     thread.start_new_thread(link, (2750, 2800))
    #     thread.start_new_thread(link, (2800, 2850))
    #     thread.start_new_thread(link, (2850, 2900))
    #     thread.start_new_thread(link, (2900, 2950))
    #     thread.start_new_thread(link, (2950, 3000))
    #     thread.start_new_thread(link, (3000, 3050))
    #     thread.start_new_thread(link, (3050, 3100))
    #     thread.start_new_thread(link, (3100, 3150))
    #     thread.start_new_thread(link, (3150, 3200))
    #     thread.start_new_thread(link, (3200, 3250))
    #     thread.start_new_thread(link, (3250, 3300))
    #     thread.start_new_thread(link, (3300, 3350))
    #     thread.start_new_thread(link, (3350, 3400))
    #     thread.start_new_thread(link, (3400, 3450))
    #     thread.start_new_thread(link, (3450, 3500))
    #     thread.start_new_thread(link, (3500, 3550))
    #     thread.start_new_thread(link, (3550, 3600))
    #     thread.start_new_thread(link, (3600, 3650))
    #     thread.start_new_thread(link, (3650, 3700))
    #     thread.start_new_thread(link, (3700, 3750))
    #     thread.start_new_thread(link, (3750, 3800))
    #     thread.start_new_thread(link, (3800, 3850))
    #     thread.start_new_thread(link, (3850, 3900))
    #     thread.start_new_thread(link, (3900, 3950))
    #     thread.start_new_thread(link, (3950, 4000))
    #     thread.start_new_thread(link, (4000, 4050))
    #     thread.start_new_thread(link, (4050, 4100))
    #     thread.start_new_thread(link, (4100, 4150))
    #     thread.start_new_thread(link, (4150, 4200))
    #     thread.start_new_thread(link, (4200, 4250))
    #     thread.start_new_thread(link, (4250, 4300))
    #     thread.start_new_thread(link, (4300, 4350))
    #     thread.start_new_thread(link, (4350, 4400))
    #     thread.start_new_thread(link, (4400, 4450))
    #     thread.start_new_thread(link, (4450, 4500))
    #     thread.start_new_thread(link, (4500, 4550))
    #     thread.start_new_thread(link, (4550, 4600))
    #     thread.start_new_thread(link, (4600, 4650))
    #     thread.start_new_thread(link, (4650, 4700))
    #     thread.start_new_thread(link, (4700, 4750))
    #     thread.start_new_thread(link, (4750, 4800))
    #     thread.start_new_thread(link, (4800, 4850))
    #     thread.start_new_thread(link, (4850, 4900))
    #     thread.start_new_thread(link, (4900, 4950))
    #     thread.start_new_thread(link, (4950, 5000))
    #     thread.start_new_thread(link, (5000, 5050))
    #     thread.start_new_thread(link, (5050, 5100))
    #     thread.start_new_thread(link, (5100, 5150))
    #     thread.start_new_thread(link, (5150, 5200))
    #     thread.start_new_thread(link, (5200, 5240))
    #     while 1:
    #         pass
    # except:
    #     print "Error: unable to start thread"