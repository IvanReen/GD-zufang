# -*- coding: utf-8 -*-
import urllib

from cw_zufang.utils.message import sendMessage_warning
from scrapy.exceptions import IgnoreRequest


class Redirect_Middleware():
    global count
    count = 1
    def process_response(self, request, response, spider):
        http_code = response.status
        if http_code // 100 == 2:
            return response
        if http_code // 100 ==3 and http_code != 304:
            global count
            if count == 1:
                sendMessage_warning()
            print('302')
            count += 1
            return request.replace(dont_dilter=True)
        if http_code // 100 == 4:
            raise IgnoreRequest('404')
        if http_code // 100 == 5:
            return request.replace(dont_filter=True)
