# -*- coding: utf-8 -*-
import json
import urllib2
import random
from time import sleep

import MySQLdb

BOTTOM = {}
UPPER = {}
COUNT = 0

def border():
    global UPPER
    global BOTTOM
    db = MySQLdb.connect(host='localhost',passwd='123aaaaaa',user='root',db='ofo',charset='utf8')
    cursor = db.cursor()
    sql = 'select * from shanghai_border_bottom'
    cursor.execute(sql)
    for row in cursor.fetchall():
        BOTTOM[round(row[0],3)] = round(row[1],3)
    sql = 'select * from shanghai_border_upper'
    cursor.execute(sql)
    for row in cursor.fetchall():
        UPPER[round(row[0],3)] = round(row[1],3)
    db.close()
    link()

def link():
    global COUNT
    global UPPER
    global BOTTOM
    for key in BOTTOM:
        spider(str(key),str(BOTTOM[key]),5,key,BOTTOM[key])


def spider(lon,lat,num,count_lon,count_lat):
    global COUNT
    global BOTTOM
    global UPPER
    http_proxy = {'http': '116.28.109.64:808'}
    url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
    payload = "?latitude=%s&longitude=%s&errMsg=getMapCenterLocation" % (lat, lon)
    url = url + payload
    headers = {
        'charset': "utf-8",
        'platform': "4",
        "referer": "https://servicewechat.com/wx40f112341ae33edb/1/",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
        'host': "mwx.mobike.com",
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'cache-control': "no-cache"
    }
    proxy = [
        '121.232.144.148:9000',
        '121.232.144.182:9000',
        '60.178.8.68:8081',
        '111.74.56.249:9000',
        '121.232.147.103:9000',
        '117.90.0.59:9000',
        '122.96.59.103:80',
        '117.79.87.165:80',
        '117.90.1.80:9000',
        '117.90.2.103:9000',
        '121.232.144.16:9000',
        '110.73.34.20:8123',
        '110.73.10.2:8123',
        '121.232.144.119:9000',
        '121.232.145.102:9000',
        '115.29.170.58:8118',
        '182.129.241.84:9000',
        '121.232.147.235:9000',
        '111.13.7.42:843',
        '121.232.144.111:9000',
        '171.92.52.248:9000',
        '171.39.39.101:8123',
        '122.96.59.103:81',
        '118.117.138.120:9000',
        '60.178.174.26:8081',
        '121.232.146.84:9000',
        '222.128.13.94:8081',
        '124.42.7.103:80',
        '121.232.144.110:9000',
        '122.96.59.103:83',
        '60.178.171.30:8081',
        '120.26.13.161:8118',
        '111.155.116.195:8123',
        '111.13.7.42:81',
        '121.232.144.168:9000',
        '121.232.148.121:9000',
        '121.232.145.93:9000',
        '121.232.147.170:9000',
        '117.90.6.203:9000',
        '121.232.144.17:9000',
        '121.232.146.2:9000',
        '171.215.226.75:9000',
        '163.125.222.129:8118',
        '122.96.59.100:80',
        '121.232.144.45:9000',
        '121.232.144.206:9000',
        '111.155.116.235:8123',
        '182.88.186.79:8123',
        '106.120.78.129:80',
        '110.73.5.199:8123',
        '121.232.144.105:9000',
        '106.120.78.129:80',
        '110.73.8.229:8123',
        '121.31.87.250:8123',
        '114.239.149.253:808',
        '121.232.146.16:9000',
        '110.73.7.103:8123',
        '121.41.175.199:80',
        '222.128.13.94:8081',
        '222.128.13.94:8081',
        '121.232.147.200:9000',
        '218.89.97.127:9000',
        '117.90.252.123:9000',
        '121.232.147.206:9000',
        '121.232.146.12:9000',
        '222.208.66.14:9000',
        '121.232.147.206:9000',
        '121.232.145.93:9000',
        '118.178.227.171:80',
        '121.31.103.138:8123',
        '110.73.34.186:8123',
        '121.31.152.122:8123',
        '116.28.109.64:808',
        '210.76.163.216:8118',
        '171.215.226.90:9000',
        '121.232.194.78:9000',
        '223.240.208.87:3128',
        '125.118.78.177:808',
        '60.178.1.60:8081',
        '123.57.184.70:8081',
        '210.76.163.216:8118',
        '121.40.34.84:8118',
        '121.232.144.147:9000',
        '119.23.63.152:8118',
        '121.31.148.205:8123',
        '171.92.52.201:9000',
        '110.243.68.171:9999',
        '180.173.109.149:8118',
        '182.141.46.93:9000',
        '210.76.163.216:8118',
        '221.230.7.59:9000',
        '121.232.146.139:9000',
        '121.232.145.43:9000',
        '118.117.139.117:9000',
        '121.232.146.205:9000',
        '121.232.147.112:9000',
        '202.141.161.30:8118',
        '117.90.0.205:9000',
        '121.232.144.156:9000',
        '122.96.59.105:82',
        '122.96.59.106:80',
        '222.208.66.14:9000',
        '111.12.96.188:80',
        '115.213.1.83:8998',
        '60.178.137.158:8081',
        '117.90.3.185:9000',
        '117.90.1.204:9000',
        '110.73.48.146:8123',
        '111.13.7.42:83',
        '118.178.227.171:80',
        '182.42.46.43:808',
        '111.74.56.249:9000',
        '111.74.56.249:9000',
        '122.96.59.105:82',
        '117.90.2.208:9000',
        '121.232.146.149:9000',
        '60.178.13.75:8081',
        '182.129.243.22:9000',
        '118.117.139.86:9000',
        '110.73.35.180:8123',
        '110.73.49.171:8123',
        '117.90.6.213:9000',
        '121.232.148.239:9000',
        '183.240.87.229:80',
        '117.90.1.22:9000',
        '114.239.148.34:808',
        '60.178.139.245:8081',
        '110.73.2.58:8123',
        '171.39.73.250:8123',
        '121.232.146.201:9000',
        '220.191.103.108:808',
        '121.232.147.222:9000',
        '222.208.83.91:9000',
        '120.27.151.13:8889',
        '122.96.59.100:80',
        '110.73.41.214:8123',
        '121.232.147.146:9000',
        '121.232.194.64:9000',
        '117.90.0.41:9000',
        '121.232.147.244:9000',
        '60.178.12.46:8081',
        '60.178.171.219:8081',
        '121.232.147.219:9000',
        '122.96.59.100:81',
        '111.13.7.42:80',
        '113.140.25.4:81',
        '121.232.145.33:9000',
        '121.232.145.223:9000',
        '110.73.33.147:8123',
        '123.169.84.88:808',
        '120.27.49.85:8090',
        '122.193.14.114:82',
        '121.232.145.104:9000',
        '171.38.36.78:8123',
        '163.125.222.240:8118',
        '114.230.31.225:3128',
        '171.92.4.67:9000',
        '121.232.147.247:9000',
        '121.232.146.148:9000',
        '121.232.144.201:9000',
        '121.232.145.251:9000',
        '110.73.55.150:8123',
        '112.33.7.9:8081',
        '115.207.7.173:808',
        '122.96.59.100:80',
    ]
    temp = random.randint(0, 160)
    http_proxy['http'] = proxy[temp]
    proxy = urllib2.ProxyHandler(http_proxy)
    opener = urllib2.build_opener(proxy)
    request = urllib2.Request(url, headers=headers)
    try:
        response = opener.open(request, timeout=0.6)
        COUNT= COUNT+1
        info = response.read()
        # print info
        info = json.loads(info)
        bikes = info['object']
        bikes_size = len(bikes)
        print (str(COUNT)+'th: '+str(num)+"("+lon+","+lat+")---"+str(bikes_size))
        if(bikes_size!=0):
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            cursor = db.cursor()
            sql = "insert into ofo.shanghai_valid (distX,distY,num) values (%s,%s,%s) on duplicate key update num = %s"
            param = (lon,lat,str(bikes_size),str(bikes_size))
            cursor.execute(sql,param)
            db.commit()
            db.close()
            pass
        for bike in bikes:
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            cursor = db.cursor()
            sql = "insert into ofo_address (distX,distY,bikeIds,save_time) values (%s,%s,%s,'2017-08-04 22:02:00') on duplicate key update distY = %s"
            param = (str(bike['distX']),str(bike['distY']),str(bike['bikeIds']),str(bike['distY']))
            cursor.execute(sql,param)
            db.commit()
            db.close()
        next_lat=count_lat+0.002
        if next_lat<UPPER[count_lon]:
            spider(lon,str(next_lat),5,count_lon,next_lat)
            # print ("%f , %f : %s"%(bike['distY'],bike['distX'],bike['bikeIds']))
    except Exception as ex:
        print ex.message
        num = num-1
        if num <= 2:
            print ("die total"+str(http_proxy['http']))
            next_lat = count_lat + 0.002
            if next_lat < UPPER[count_lon]:
                spider(lon, str(next_lat), 5, count_lon, next_lat)
        else:
            spider(lon,lat,num,count_lon,count_lat)
        pass

if __name__ == '__main__':
    # link()
    border()