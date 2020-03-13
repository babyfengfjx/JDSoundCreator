import wx_sdk
import base64
import json
import re
import time
import os


def to_mp3(string, name):
    """
    将传入的string字符串处理成mp3音频文件
    @param string: 要转换的文字
    @param name: 要保存的mp3的名称
    @return: 无返回
    """
    try:
        url = 'https://aiapi.jd.com/jdai/tts_vip'
        skey = 'ae90bdffed42ed109865ca2f16a0b8c2'  # 这个secretkey京东的控制台可以查看到
        print('输入的文字内容为：\n{}\n{}'.format(string,'*'*50))
        bodyStr = string.encode('utf-8')  # 传入接口处理的文字，需要先编码成utf-8字节码
        params = {
            'Service-Type': 'synthesis',
            'Request-Id': '2c4dc6e2-e1c5-11e8-a867-040973d59110',
            'Sequence-Id': '-1',
            'Protocol': '1',
            'Net-State': '2',
            'Applicator': '1',
            'Property': '{"platform":"Linux","version":"0.0.0.1","parameters":{"aue":"3","vol":"1.0","sr":"24000","sp":"0.9","tim":"0","tte":"1"}}',
            'appkey': 'e408b88d69dcd1039d9a02b7d4a3500b',
            'secretkey': skey,
            'sign': wx_sdk.sign(skey)  # 这是SDK自带的方法，用于生成sign值的。
        }
        print('接口调用中……')
        response = wx_sdk.wx_post_req(url, params, bodyStr=bodyStr)  # 这个是SDK写的方式，直接调用。
        rep = response.json()  # 通过json格式解析一下返回体，更好的进行后续处理。
        code = rep['code']
        remain = rep['remain']
        msg = rep['msg']
        print('返回状态码是：{}\n调用次数还剩：{}次\n{}'.format(code, remain, msg))
        # print(rep)
        mp = rep['result']['audio']  # 因为json解析后就是一个字典，其中audio是嵌套字典，所以取值有两层。
        mp = base64.b64decode(mp)  # 查看京东接口文档，发现音频是base64编码方式，这里要用到base64库中的b64decode方法，直接传字符串即可解码。
        print('MP3文件开始写入……')
        # 下面先判断文件夹是否存在，不存在就创建一个，os模块中os.path.exists()判断
        if not os.path.exists(r'..\mp3'):  #
            os.mkdir(r'..\mp3')
        # 使用相对路径来处理，便于程序的移植
        with open(r'..\mp3\{}.mp3'.format(name), 'wb') as mpwrite:
            mpwrite.write(mp)
            print('{}\n mp3文件【写入成功！】'.format(name))
    except Exception as error:
        print('处理文件《{}》时出错，请查看日志记录'.format(name))
        # 并将错误记录写入日志文件
        # if not os.path.exists(r'..\mp3\log.txt'):
        #     os
        with open(r'..\log.txt', 'a') as w:
            w.write('处理文件{}时出错，请查看日志记录----{}\n报错内容：{}\n'.format(name,
                                                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()
                                                                    ),error))
        print(error)
        print('*'*50)

def test_to_mp3(string, name):
    print('*' * 50)
    print()
    print('待处理文字：\n\n', string)
    print('*' * 50)
    print()
    print('mp3名称：', name)
def string_oprator(fun):
    """
    批量读取文档中段落，并处理成MP3文件。
    @param fun:传的to-mp3函数名
    @return:无返回
    """
    count = 0
    with open(r'C:\Users\jinxiong\Desktop\shangzhuang\file_test .txt', 'r') as f:
        s = ''
        count = 0
        while True:
            cont = f.readline().replace('\n', '')
            if cont == '':
                count += 1
                if count >= 50:
                    print('文件处理完成……')
                    break

            if '标题' in cont:
                titlename = cont.split('：')[0].strip() + '、'+cont.split('：')[-1].strip()
                continue
            if '********' in cont:
                if '所需资料' in s:
                    name = titlename + '_所需资料'
                    fun(s, name)
                if '办理流程' in s:
                    name = titlename + '_办理流程'
                    fun(s, name)
                s = ''  #处理完一段就将字符串置空，这个很重要。
            else:
                s += cont
if __name__ == '__main__':
    string_oprator(to_mp3)
