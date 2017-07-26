# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface-test
# author: "Lei Yong" 
# creation time: 2017/7/26 0026 15:59
# Email: leiyong711@163.com
# from Interface.excel_r import excel
# from Interface import excel_w

import json
import sys
import urllib     # 把这两个库导入
import urllib2

from Interface.excel_r import excel

reload(sys)
sys.setdefaultencoding('utf-8')

def POST(url,data):
    data  # 根据api文档提供的参数，来获取一下,把这些参数值存在一个dict里
    data = urllib.urlencode(data)  # 把参数进行编码
    url2 = urllib2.Request(url,data)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    response = urllib2.urlopen(url2)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
    print type(response)
    apicontent = response.read()  # 将响应内容用read()读取出来
    print type(apicontent)
    return apicontent
    # json.loads(apicontent)['code']

def GET(url,api):
    url = url + api
    req = urllib2.Request(url)
    # print req
    res_data = urllib2.urlopen(req)
    # print res_data
    res = res_data.read()
    return res

# if __name__ == "__main__":
    # GET('http://www.tuling123.com/openapi/api','?info=你好&key=305122eaa84142aa8b076a962ca87523')
    # POST('http://www.tuling123.com/openapi/api',{'info':'你好','key':'305122eaa84142aa8b076a962ca87523'})


def ks():
    asp = excel()
    for i in range(1,len(asp)):
        if asp[i][5] == 'POST':
            a = POST(asp[i][2], {'key': asp[i][3], 'info': asp[i][4]})
            # print type(a)
            if json.loads(a)['code'] == asp[i][6]:
                # asp[i][7] = json.loads(a)['text']
                asp[i][7] = a
                asp[i][8] = 'Pass'
                spc = asp
                # print spc
            else:
                asp[i][7] = a
                asp[i][8] = 'Fail'
                spc = asp
                # print spc

        else:
            # print '-'*20
            a = GET(asp[i][2], '?info=' + asp[i][4] + '&key=' + asp[i][3])
            # print type(a)
            # print a
            if json.loads(a)['code'] == asp[i][6]:
                asp[i][7] = a
                asp[i][8] = 'Pass'
                spc = asp
                # print spc
            else:
                asp[i][7] = a
                asp[i][8] = 'Fail'
                spc = asp
                # print spc
            # print '-' * 20
    return spc