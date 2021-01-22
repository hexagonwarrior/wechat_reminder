#!/usr/bin/env python2
#-*- coding:utf-8 -*-
#import pdb
#pdb.set_trace()

import itchat
from itchat.content import *
from aip import AipOcr
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # 返回同样的文本消息
    print msg['Text']

# 注册监听群中信息，如果是图片，则进行识别
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    print msg['FileName']
    picname = msg['FileName']
    # 准备百度识别接口
    # 你的 APPID AK SK
    APP_ID = '23076358'
    API_KEY = 'AwSc1KyC3ZZaM0pnsNd7QCf8'
    SECRET_KEY = 'TEKKTuAYRe8bAtGniBa1PIPr1ytdFXri'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    image = get_file_content(picname)

    ''' # 如果有可选参数
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    '''
    
    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    # 识别图片中名字
    result = client.basicGeneral(image)
    at = []
    for w in result['words_result']:
        x = w['words']
        print x
        for name in memberlist:
            # print x # tuple
            # print name # 汉字
            if x.find(name.decode('utf-8')) != -1:
                at.append(name)

    # 找到目标群组，然后发送消息
    roomslist = itchat.get_chatrooms(update=True)
    for r in roomslist:
        # print r['NickName']
        # if r['NickName'] == u'软件学院2020级非全日制':
        if r['NickName'] == u'北航非全测试群':
            chatGtoupName = r['UserName'] # 系统的群id
            for a in at:
                print a
                itchat.send_msg((a), chatGtoupName)
                time.sleep(1)
        

if __name__ == '__main__':
    memberlist = []
    # 读取memberlist
    cnt = 0
    with open('memberlist.txt', 'r') as f:
        for l in f.readlines():
            name = l.strip()
            memberlist.append(name)
    print '---------------------'
    
    itchat.auto_login(hotReload='True')
    itchat.run()
    
    
