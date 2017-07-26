# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Interface-test
# author: "Lei Yong" 
# creation time: 2017/6/8 0008 18:43
# Email: leiyong711@163.com
import sys
import time
import datetime
reload(sys)
sys.setdefaultencoding('utf8')
def ceshixiangqing(nq,nw,ne,nr,nt,ny,nu,ni,no,np,na,ns,nd,nf):  #(nq,nw,ne,nr,nt,ny,nu,ni,no,np,na,ns,nd,nf):
    xiangqing = '''
    <!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>接口测试报告</title>
		<style type="text/css">
			td{ width:40px; height:50px;}
		</style>
	</head>
	<body>

<div style='width: 1170px;margin-left:20'>
<h1>接口测试的结果</h1>

<p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			        </span></p>
			    <p ><strong>测试详情如下</strong></p>  </div>


		<p>&nbsp;</p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
		<tr >
            <td ><strong>用例ID&nbsp;</strong></td>
            <td><strong>用例名字</strong></td>
            <td><strong>key</strong></td>
            <td><strong>请求内容</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>实际返回</strong></td>
            <td><strong>结果</strong></td>
        </tr>

		<tr>
            <td>%s</td>
            <td>%s</td>

            <td>%s</td>
            <td>%s
           </td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>

	</table>

    </body>
    </html>
'''% (nq,nw,ne,nr,nt,ny,nu,ni,no,np,na,ns,nd,nf)
    return xiangqing
a = datetime.datetime.now()
time.sleep(1)
b = datetime.datetime.now()
# 开始时间、结束时间、耗时、结果pass、fail、
# 用例id、用例名字、key、请求内容、url、请求方式、预期结果、实际返回、结果


# def create():
#     texts = title('12','23','11','5','6','1.0',u'\u56fe\u7075api\u63a5\u53e3',u'sasa',u'\u4f60\u597d\u554a',
#                   u'http://www.tuling123.com/openapi/api','POST',40001,'{"code":40001,"text":}','pass')
#     with open('..\\lei.html','wb') as f:
#         f.write(texts.encode('utf-8'))
# [1.0, u'\u56fe\u7075api\u63a5\u53e3', u'http://www.tuling123.com/openapi/api', u'sasa', u'\u4f60\u597d\u554a', u'POST', 40001.0, '{"code":40001,"text":"\xe4\xba\xb2\xe7\x88\xb1\xe7\x9a\x84\xef\xbc\x8ckey\xe4\xb8\x8d\xe5\xaf\xb9\xe5\x93\xa6\xe3\x80\x82"}', 'Pass']
# def relust(titles,starttime,endtime,passge,fail,id,name,key,coneent,url,meth,yuqi,json,relust):
#     text = title(titles) + connent
#
#


def create():
	texts=ceshixiangqing(a, b, b-a, 3, 2, 1, u'\u56fe\u7075api\u63a5\u53e3',
 u'sasa', u'\u4f60\u597d\u554a', u'http://www.tuling123.com/openapi/api',
 'POST', 40001, '{"code":100000,"text":"楼主腿烫伤了躺床上休息，老公趴 床上拔 罐，闺女看我俩这样快哭了:“你们俩都生病了，我好担心！” 老公一脸自豪:“这小棉袄没白 养” “你们俩都生病了明天谁送我去幼儿园啊？呜呜呜”小家伙急哭了 哎，夏天来了，小棉袄烧心啊"}','pass')
	with open('..\\lei.html','wb') as f:
		f.write(texts.encode('utf-8'))

