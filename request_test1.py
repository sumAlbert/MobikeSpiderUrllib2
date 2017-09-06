import random
import urllib
import urllib2

import requests
import time

proxies=[]

def spider():
    global proxies
    try:
        random_proxy = random.choice(proxies)
        proxie = {
            'https': random_proxy
        }
        url1 = 'https://sojump.com/m/15669479.aspx'
        headers={
            'Host': 'sojump.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cookie': 'UM_distinctid=15e510ea84a380-08e4da64f8c5ae8-370d466d-2c600-15e510ea84c33d; CNZZDATA4478442=cnzz_eid%3D855102626-1504593355-%26ntime%3D1504620355; LastActivityJoin=15669479,101006819862; join_15669479=1; jac15669479=99047243; award_15669479=1; jaward101006962742=1; .ASPXANONYMOUS=QBc--K5c0wEkAAAAMWE4NTQ0YzYtYWFiNS00OGZjLTgzOTgtMDUyZDNlMThjOGMwfdumwlqXDF3tcreIoGP7oJjZLcc1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        res1 = requests.post(url1, headers=headers,proxies=proxie)
        print res1.text
        pw=res1.cookies['jac15669479']
        url2 = 'https://sojump.com/handler/processjq.ashx?curid=15669479&starttime=2017%2F9%2F6%20' + str(time.strftime("%H")) + '%3A' + time.strftime("%M") + '%3A' + time.strftime("%S") + '&source=directphone&submittype=1&rn=3029770955.' + pw + '&iwx=1&t=' + str(int(round(time.time() * 1000)))
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
            'Referer': 'https://sojump.com/m/15669479.aspx',
            'Cookie': 'UM_distinctid=15e510ea84a380-08e4da64f8c5ae8-370d466d-2c600-15e510ea84c33d; CNZZDATA4478442=cnzz_eid%3D855102626-1504593355-%26ntime%3D1504620355; jac15669479='+pw+'; LastActivityJoin=15669479,101006819862; join_15669479=1; award_15669479=1; jaward101006962742=1; .ASPXANONYMOUS=QBc--K5c0wEkAAAAMWE4NTQ0YzYtYWFiNS00OGZjLTgzOTgtMDUyZDNlMThjOGMwfdumwlqXDF3tcreIoGP7oJjZLcc1'
        }
        values={"submitdata":"1$1}2$1}3$1}4$1}5$1}6$1}7$1}8$5}9$5}10$1}11$1}12$1}13$10}14$1<5,2<5,3<5,4<5,5<5,6<5"}
        data = urllib.urlencode(values)
        res2 = requests.post(url2,headers=headers2,data=values,proxies=proxie)
        print res2.text
    except Exception as ex:
        print ex.message
def getProxy():
    global proxies
    url='http://dev.kuaidaili.com/api/getproxy/?orderid=960468106685540&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_ha=1&sep=4'
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
    getProxy()
    spider()
    pass
