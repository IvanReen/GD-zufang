# -*- coding: utf-8 -*-
import random

from cw_zufang.utils.GetProxyIp import GetIps


class ProxyMiddleware():
    global count
    count = 1
    global ips
    ips = []
    def process_request(self, request, spider):
        global count
        global ips
        if count == 1:
            ips = GetIps()
        elif count % 100 == 0:
            ips = []
            ips = GetIps()
        try:
            num = random.randint(0, len(ips))
            ress = 'http://' + ips[num]
        except:
            pass
        else:
            request.meta['proxy'] = str(ress)
            count += 1