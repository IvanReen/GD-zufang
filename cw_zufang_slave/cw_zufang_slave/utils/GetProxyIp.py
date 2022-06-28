# -*- coding: utf-8 -*-

import requests
def GetIps():
    global count
    url ='http://139.199.182.250:8000/?types=0&count=300'
    ips=requests.get(url)
    return [f'{ip[0]}:{ip[1]}' for ip in eval(ips.content)]

GetIps()
