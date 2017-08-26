# -*- coding: utf-8 -*-
import json
import random
import threading
import urllib2
import MySQLdb
import time
import thread

SAVE_TIME=''
DISTX =[]
DISTY =[]
COUNT = 0
proxies = [
]
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
    sql = 'SELECT * FROM putuo_address_info'
    cursor.execute(sql)
    for row in cursor.fetchall():
        DISTX.append(row[1])
        DISTY.append(row[2])
    db.close()
def address2():
    global DISTX
    global DISTY
    for x in xrange(0,131):
        distx=x*0.001+121.330
        for y in xrange(0,101):
            disty=y*0.001+31.220
            DISTX.append(distx)
            DISTY.append(disty)
def link(bottom,upper):
    global DISTY
    global DISTX
    global COUNT
    global threading_lock
    for num in xrange(bottom,upper):
        # 12321
        if num<5248:
            lon = DISTX[num]
            lat = DISTY[num]
            spider(lon,lat,60)
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
    # urllib2.install_opener(opener)
    request = urllib2.Request(url, headers=headers)
    try:
        # html = urllib2.urlopen(request,timeout=3)
        html = opener.open(request,timeout=2)
        info = html.read()
        info_out=info
        info = json.loads(info)
        bicycle = info['bicycle']
        message = bicycle['message']
        if message=='ok':
            bicycles = bicycle['bicycles']
            items = bicycles['item']
            threading_lock.acquire()
            COUNT = COUNT + 1
            print COUNT
            print info_out
            threading_lock.release()
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            for item in items:
                cursor = db.cursor()
                sql = "insert into putuo_mobike_address3 (distX,distY,bikeIds,source,save_time,flag) values (%s,%s,%s,%s,%s,'170825_1') on duplicate key update distY = %s"
                param = (str(item['x']), str(item['y']),str(item['id']),str(item['source']),str(SAVE_TIME),str(item['y']))
                cursor.execute(sql, param)
                db.commit()
            db.close()
        else:
            pass
    except Exception as ex:
        print str(Exception)
        print ex.message
        if(num>0):
            print ("again")
            num=num-1
            if len(proxies)>3:
                threading_lock.acquire()
                print ('proxy_num:'+str(len(proxies)))
                if proxies.count(random_proxy)>0:
                    proxies.remove(random_proxy)
                threading_lock.release()
            spider(lon,lat,num)
        else:
            threading_lock.acquire()
            COUNT = COUNT + 1
            print "die"
            threading_lock.release()
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
def time_start_lock():
    global time_lock
    time_lock='true'
    time.sleep(180)
    time_lock='false'
def time_stop_lock():
    global stop_lock
    time.sleep(3660)
    stop_lock='true'

if __name__ == '__main__':
    thread.start_new_thread(time_stop_lock, ())
    address()
    threads_1=[]
    threads_2=[]
    threads_3=[]
    threads_4=[]
    threads_5=[]
    threads_6=[]
    try:
        while 1:
            SAVE_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            thread.start_new_thread(time_start_lock ,())
            COUNT=0
            getProxy()
            for num in xrange(0, 128):
                start_num = num * 41
                stop_num = num * 41 + 41
                myThread = MyThread(start_num, stop_num)
                if num < 43:
                    threads_1.append(myThread)
                elif num < 86:
                    threads_2.append(myThread)
                elif num < 128:
                    threads_3.append(myThread)
                # elif num < 111:
                #     threads_4.append(myThread)
                # elif num < 122:
                #     threads_5.append(myThread)
                else:
                    threads_6.append(myThread)
            for t in threads_1:
                t.start()
            for t in threads_1:
                t.join()
            while len(threads_1)!=0:
                threads_1.pop()
            time.sleep(1)
            getProxy()
            print len(proxies)
            for t in threads_2:
                t.start()
            for t in threads_2:
                t.join()
            while len(threads_2)!=0:
                threads_2.pop()
            time.sleep(1)
            getProxy()
            for t in threads_3:
                t.start()
            for t in threads_3:
                t.join()
            while len(threads_3)!=0:
                threads_3.pop()
            localtime = time.asctime(time.localtime(time.time()))
            print "本地时间为 :", localtime
            # time.sleep(2)
            # getProxy()
            # for t in threads_4:
            #     t.start()
            # for t in threads_4:
            #     t.join()
            # while len(threads_4)!=0:
            #     threads_4.pop()
            # time.sleep(2)
            # getProxy()
            # for t in threads_5:
            #     t.start()
            # for t in threads_5:
            #     t.join()
            # while len(threads_5)!=0:
            #     threads_5.pop()
            # getProxy()
            # for t in threads_6:
            #     t.start()
            # for t in threads_6:
            #     t.join()
            # while len(threads_6)!=0:
            #     threads_6.pop()
            while 1:
                time.sleep(1)
                print (time_lock=='false')
                if time_lock=='false':
                    break
            if stop_lock=='true':
                break
            pass
    except Exception as ex:
        print ex.message