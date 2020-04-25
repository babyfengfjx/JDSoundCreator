#!/usr/bin/python
# -*- coding: utf-8 -*-
# 本代码仅供参考，请根据实际情况进行调整
import wx_sdk
import base64
import json
import re

string = '''所需资料：
1、 注销表。




2、 死亡证明。




3、 参保人身份证或户口本复印件1份。




4、 继承人身份证或户口本复印件1份。




5、 继承人信用社帐号复印件1份。




6、 参保人与继承人关系证明。
'''

def to_mp3(string, name):
    url = 'https://aiapi.jd.com/jdai/tts_vip'
    skey = 'ae90bdffed42ed109865ca2f16a0b8c2'
    bodyStr = string.encode('utf-8')
    params = {
        'Service-Type': 'synthesis',
        'Request-Id': '2c4dc6e2-e1c5-11e8-a867-040973d59110',
        'Sequence-Id': '-1',
        'Protocol': '1',
        'Net-State': '2',
        'Applicator': '1',
        'Property': '{"platform":"Linux","version":"0.0.0.1","parameters":{"aue":"3","vol":"1.0","sr":"24000","sp":"0.8","tim":"0","tte":"1"}}',
        'appkey': 'e408b88d69dcd1039d9a02b7d4a3500b',
        'secretkey': skey,
        'sign': wx_sdk.sign(skey)
    }
    print('接口调用中……')
    response = wx_sdk.wx_post_req(url, params, bodyStr=bodyStr)
    rep = response.json()
    print(rep)
    mp = rep['result']['audio']
    code = rep['code']
    remain=rep['remain']
    msg=rep['msg']
    print('返回状态码是：{}\n调用次数还剩：{}次\n{}'.format(code,remain,msg))
    mp = base64.b64decode(mp)
    print('开始写入……')
    with open(r'{}.mp3'.format(name), 'wb') as mpwrite:
        mpwrite.write(mp)
        print('{}\n mp3文件【写入成功！】'.format(name))

if __name__ == '__main__':
    to_mp3(string, '城乡居民最低生活保障待遇审核')

