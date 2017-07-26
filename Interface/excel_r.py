# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface-test
# author: "Lei Yong" 
# creation time: 2017/6/8 0008 14:38
# Email: leiyong711@163.com
import xlrd


def excel():
    fname = "Case\\test.xlsx"
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name('Sheet1')
    except:
        print "%没有表名为Sheet1的" % fname
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print (nrows), (ncols)
    a = []
    for i in range(0, nrows):
        c = sh.row_values(i)
        # if i == 0:
        #     continue
        # else:
        #     c[0] = int(c[0])
        #     c[6] = int(c[6])
        a.append(c)
    return a
#     print a
a = excel()
print a[1][0]
