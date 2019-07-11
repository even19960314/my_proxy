# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:57:33 2019

>>> x = get_proxies()

>>> {'port': '43437', 'ip': '115.211.230.124'}



以下是熊猫代理返回的格式

     {'code': '0',
     'msg': 'ok',
     'obj': [{'port': '43437', 'ip': '115.211.230.124'}],
     'errno': 0,
     'data': [None]}

obj是返回代理ip的列表zpj


@author: 
"""
import time
import requests



#proxy_url,是熊猫代理的api接口，
proxy_url = 'http://www.xiongmaodaili.com/xiongmao-web/api/glip?...'


def get_proxies(proxy_url = proxy_url):
    
    '''
    proxy_url: 代理网站的api
    
    return : {'port': '43437', 'ip': '115.211.230.124'}
        
        以下是熊猫代理返回的代理格式
        
    {'code': '0',
     'msg': 'ok',
     'obj': [{'port': '43437', 'ip': '115.211.230.124'}],#这里是一个代理ip
     'errno': 0,
     'data': [None]}
    
    '''
    time.sleep(1)
    return requests.get(proxy_url).json()['obj'][0]


if __name__ == '__main__':
    
    
#    x = get_proxies()
    
    pass
    












