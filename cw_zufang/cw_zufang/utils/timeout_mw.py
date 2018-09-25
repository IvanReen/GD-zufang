# -*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.downloadtimeout import DownloadTimeoutMiddleware


class Timeout_Middleware(DownloadTimeoutMiddleware):
    def process_exception(self, request, exception, spider):
        # print("***the downloader has exception")
        print(exception)
        return request.replace(dont_filter=True)