#!/usr/bin/env python2
#-*- coding:utf-8 -*-
#import pdb
#pdb.set_trace()

import itchat, time
import sys
from itchat.content import *
itchat.auto_login(hotReload=True)
wish_list = [u"二零二一金牛到，在这阖家团圆之际，祝您和您的家人 身体健康 新年快乐！"]

SINCERE_WISH = wish_list[0]
friendList = itchat.get_friends(update=True)[1:]

for g in range(0, len(friendList)):
    itchat.send(SINCERE_WISH, friendList[g]['UserName'])
    print((friendList[g]['RemarkName'] or friendList[g]['Nickname']), '己发送')
    sys.stout.write(str[g+1]+"/"+str(len(friendList))+"\r")
    sys.stdout.flush()
    time.sleep(2)
print('done')

