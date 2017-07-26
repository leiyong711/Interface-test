# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: rw_data-test
# author: "Lei Yong" 
# creation time: 2017/6/8 0008 16:17
# Email: leiyong711@163.com
import os
import time

from pyExcelerator import *

from Public.main import ks


# def excel():
#     fname = "..\\Case\\test.xlsx"
#     bk = xlrd.open_workbook(fname)
#     try:
#         sh = bk.sheet_by_name('Sheet1')
#     except:
#         print "%没有表名为Sheet1的" % fname
#     # 获取行数
#     # nrows = sh.nrows
#     # # 获取列数
#     # ncols = sh.ncols
#     # print (nrows),(ncols)
#     return sh.row_values(0)
class apc:
    def exceslw(self):
        aps = [u'用例ID', u'用例名', u'url', u'参数值', u'请求方式', u'期望', u'实际返回', u'结果']
        # print aps
        w = Workbook()  #创建一个工作簿
        ws = w.add_sheet('Hey, Hades')  #创建一个工作表
        # ws = copy('..\\Case\\test.xlsx')
        pc = ks()
        # print pc
        for i in range(len(pc)):
            for j in range(len(pc[i])):
            #     ws.write(i,j,aps[j]) #在1行1列写入bit
                a = pc[i][j]
                if j == 6:
                    ws.write(i, j, a.decode('utf-8'))  # 在1行1列写入bit
                else:
                    ws.write(i, j, a)
        timestr = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        a = os.path.exists('..\\report\\%s'%timestr)
        if a == False:
            os.makedirs('..\\report\\%s'%timestr)
        w.save('..\\report\\%s\\case_result.xlsx'%timestr)  #保存
        return pc


