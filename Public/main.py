# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: rw_data-test
# author: "Lei Yong" 
# creation time: 2017/7/26 0026 15:59
# Email: leiyong711@163.com
# from rw_data.excel_r import excel
# from rw_data import excel_w

import json
import sys
import urllib     # 把这两个库导入
import urllib2

from rw_data.excel_r import excel

reload(sys)
sys.setdefaultencoding('utf-8')

def POST(url,data):
    data_code = urllib.urlencode(data)  # 把参数进行编码
    # url2 = urllib2.Request(url,data1)  # 用.Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    response = urllib2.urlopen(url,data_code)  # 用.urlopen打开上一步返回的结果，得到请求后的响应内容
    apicontent = response.read()  # 将响应内容用read()读取出来
    return apicontent
    # json.loads(apicontent)['code']

def GET(url,api):
    url = url + '?' + api
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
        request_type = asp[i][4].upper()
        if request_type == 'POST':
            l = []
            data = {}
            jiequ = asp[i][3].split(',')
            for k in range(len(jiequ)):
                spli = jiequ[k].split('=')
                l.append([])
                for j in range(len(spli)):
                    l[k].append(spli[j])
                data.setdefault(l[k][0], l[k][1])
            returned_value = POST(asp[i][2],data)
            fanhui = cmp(returned_value, asp[i][5])
            if fanhui == 1:
                asp[i][6] = returned_value
                asp[i][7] = 'Pass'
                spc = asp
            elif fanhui == -1:
                asp[i][6] = returned_value
                asp[i][7] = 'Fail'
                spc = asp

            else:
                asp[i][6] = returned_value
                asp[i][7] = 'error'
                spc = asp

        elif request_type == 'GET':
            data = asp[i][3].replace(',', '&')
            returned_value = GET(asp[i][2], data)
            fanhui = cmp(returned_value, asp[i][5])
            if fanhui == 1:
                asp[i][6] = returned_value
                asp[i][7] = 'Pass'
                spc = asp
            elif fanhui == -1:
                asp[i][6] = returned_value
                asp[i][7] = 'Fail'
                spc = asp

            else:
                asp[i][6] = returned_value
                asp[i][7] = 'error'
                spc = asp


        else:
            asp[i][6] = u'请求类型错误'
            asp[i][7] = 'error'
            spc = asp

    return spc
