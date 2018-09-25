# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendMessage_warning():
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('small_pupil@163.com', 'RCWzb1010')
    msg = MIMEText('爬虫slave被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = 'small_pupil@163.com <small_pupil@163.com>'
    msg['Subject'] = Header(u'爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = u'seven <1178820116@qq.com>'
    server.sendmail('small_pupil@163.com', ['1178820116@qq.com'], msg.as_string())
