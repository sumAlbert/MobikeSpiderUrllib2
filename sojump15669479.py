# -*- coding: utf-8 -*-
# 0.001
import cookielib
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

proxies = []

def spider():
    global proxies
    random_proxy = random.choice(proxies)
    # proxy_support = urllib2.ProxyHandler({"https": random_proxy})
    proxy_support = urllib2.ProxyHandler({})
    url='https://sojump.com/m/15669479.aspx'
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(proxy_support,handler)
    headers={
        'Host': 'sojump.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': 'UM_distinctid=15e510ea84a380-08e4da64f8c5ae8-370d466d-2c600-15e510ea84c33d; CNZZDATA4478442=cnzz_eid%3D855102626-1504593355-%26ntime%3D1504620355; LastActivityJoin=15669479,101006819862; join_15669479=1; jac15669479=99047243; award_15669479=1; jaward101006962742=1; .ASPXANONYMOUS=QBc--K5c0wEkAAAAMWE4NTQ0YzYtYWFiNS00OGZjLTgzOTgtMDUyZDNlMThjOGMwfdumwlqXDF3tcreIoGP7oJjZLcc1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    try:
        request = urllib2.Request(url, headers=headers)
        response = opener.open(request,timeout=10)
        result = response.read()
        pw = ''
        for item in cookie:
            print 'name:' + item.name + '-value:' + item.value
            pw=item.value
        url2 ='https://sojump.com/handler/processjq.ashx?curid=15669479&starttime=2017%2F9%2F6%20'+str(time.strftime("%H"))+'%3A'+'00'+'%3A'+'00'+'&source=directphone&submittype=1&rn=3029770955.'+pw+'&iwx=1&t='+str(int(round(time.time() * 1000)))
        print url2
        headers2 = {
            'Host': 'sojump.com',
            'Accept': 'text/plain, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://sojump.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Connection': ' keep-alive',
            'Referer': 'https://sojump.com/m/15669479.aspx',
            'Cookie': 'UM_distinctid=15e510ea84a380-08e4da64f8c5ae8-370d466d-2c600-15e510ea84c33d; CNZZDATA4478442=cnzz_eid%3D855102626-1504593355-%26ntime%3D1504620355; jac15669479='+pw+'; LastActivityJoin=15669479,101006819862; join_15669479=1; award_15669479=1; jaward101006962742=1; .ASPXANONYMOUS=QBc--K5c0wEkAAAAMWE4NTQ0YzYtYWFiNS00OGZjLTgzOTgtMDUyZDNlMThjOGMwfdumwlqXDF3tcreIoGP7oJjZLcc1'
        }
        values={"submitdata":"1$1}2$1}3$1}4$1}5$1}6$1}7$1}8$5}9$5}10$1}11$1}12$1}13$10}14$1<5,2<5,3<5,4<5,5<5,6<5"}
        data = urllib.urlencode(values)
        # proxy_support2 = urllib2.ProxyHandler({"https": random_proxy})
        proxy_support2 = urllib2.ProxyHandler({})
        opener2 = urllib2.build_opener(proxy_support2)
        request2 = urllib2.Request(url2, headers=headers2,data=data)
        html=opener2.open(request2,timeout=10)
        info=html.read()
        infoout=info
        print infoout
        time.sleep(5)
        spider()
    except Exception as ex:
        print ex.message
        traceback.print_exc()
        if proxies.count(random_proxy)>0:
            proxies.remove(random_proxy)
        print len(proxies)
        spider()

def getProxy():
    global proxies
    url='http://dev.kuaidaili.com/api/getproxy/?orderid=960468106685540&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_ha=1&sp1=1&sep=4'
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
def getAnswers():
    result=''
    for num in xrange(1,15):
        if num!=14:
            result=result+str(num)+'$'+getAnswer(num)+'}'
        else:
            result=result+str(num)+'$'+getAnswer(num)
    return result
    pass

def getAnswer(num):
    dataAnswer=random.randint(1,1000)
    print dataAnswer
    if num==1:
        if dataAnswer<477:
            return str(1)
        else:
            return str(2)
    elif num==2:
        if dataAnswer<722:
            return str(1)
        elif dataAnswer<852:
            return str(2)
        elif dataAnswer<932:
            return str(3)
        elif dataAnswer<985:
            return str(4)
        else:
            return str(5)
    elif num==3:
        if dataAnswer<788:
            return str(1)
        elif dataAnswer<982:
            return str(2)
        else:
            return str(3)
    elif num==4:
        if dataAnswer<980:
            return str(1)
        else:
            return str(2)
    elif num==5:
        dataAnswer = random.randint(1, 1000)
        result=''
        flag = 0
        if dataAnswer<856:
            flag=flag+1
            result=result+str(1)
        dataAnswer = random.randint(1, 1000)
        if dataAnswer<843:
            if flag!=0:
                result=result+'|'+str(2)
            else:
                result=result+str(2)
            flag=flag+1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer<130:
            if flag!=0:
                result=result+'|'+str(3)
            else:
                result=result+str(3)
            flag=flag+1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer<160:
            if flag!=0:
                result=result+'|'+str(4)
            else:
                result=result+str(4)
            flag=flag+1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer<320:
            if flag!=0:
                result=result+'|'+str(5)
            else:
                result=result+str(5)
            flag=flag+1
        if dataAnswer<90:
            if flag!=0:
                result=result+'|'+str(6)
            else:
                result=result+str(6)
            flag = flag + 1
        if dataAnswer<100:
            if flag!=0:
                result=result+'|'+str(7)
            else:
                result=result+str(7)
        if result=='':
            result=str(1)
        return result
    elif num == 6:
        dataAnswer = random.randint(1, 1000)
        result = ''
        flag = 0
        if dataAnswer < 497:
            flag = flag + 1
            result = result + str(1)
        dataAnswer = random.randint(1, 1000)
        if dataAnswer < 380:
            if flag != 0:
                result = result + '|' + str(2)
            else:
                result = result + str(2)
            flag = flag + 1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer < 321:
            if flag != 0:
                result = result + '|' + str(3)
            else:
                result = result + str(3)
            flag = flag + 1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer < 475:
            if flag != 0:
                result = result + '|' + str(4)
            else:
                result = result + str(4)
            flag = flag + 1
        dataAnswer = random.randint(1, 1000)
        if dataAnswer < 217:
            if flag != 0:
                result = result + '|' + str(5)
            else:
                result = result + str(5)
        if result == '':
            result = str(1)
        return result
    elif num == 7:
        if dataAnswer < 400:
            return str(1)
        elif dataAnswer < 600:
            return str(2)
        elif dataAnswer < 800:
            return str(3)
        elif dataAnswer < 900:
            return str(4)
        elif dataAnswer < 970:
            return str(5)
        else:
            return str(6)
    else:
        return ''

if __name__ == '__main__':
    # getProxy()
    # spider()
    print getAnswers()
    pass