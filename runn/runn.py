# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: rw_data-test
# author: "Lei Yong" 
# creation time: 2017/7/26 0026 16:07
# Email: leiyong711@163.com
import datetime
from rw_data.excel_w import apc
# from Public.html import create
start = datetime.datetime.now()
print '接口测试开始'
asb = apc()
asb.exceslw()
print '接口测试结束'
end = datetime.datetime.now()
Time_consuming = str(end - start)[:-7]  # 用测试结束时间-开始时间得到测试耗时，再把时间转成字符串并去掉小数部分
print '测试耗时：%s' % Time_consuming
