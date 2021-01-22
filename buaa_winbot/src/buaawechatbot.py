# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    : 
# @Software: PyCharm

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading
import time

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    # print(message)
    queue_recved_message.put(message)


# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    while True:
        message = queue_recved_message.get()
        # print(message)
        if 'msg' in message.get('type'):
            # 这里是判断收到的是消息 不是别的响应
            msg_content = message.get('data', {}).get('msg', '')
            send_or_recv = message.get('data', {}).get('send_or_recv', '')
            data_type = message.get('data', {}).get('data_type', '')
            from_member_wxid = message.get('data', {}).get('from_member_wxid', '')
            if data_type == '1' and (from_member_wxid == 'wxid_on6vrlm6mi4712' or from_member_wxid == 'wxid_kebeinngdjjr21'):
                msg = message.get('data', {}).get('msg', '')
                wxid = member_dict[msg].strip()
                print(wxid)
                
                # 测试群 23850395431@chatroom
                # 非全日制群 19442513534@chatroom
                # 小分队群 19987403427@chatroom
                wx_inst.send_text(to_user='19442513534@chatroom', msg='请%s同学打卡'%(msg), at_someone=wxid)
                time.sleep(1)

if __name__ == '__main__':
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    # print('登陆成功')
    # print(wx_inst.get_myself())

    threading.Thread(target=thread_handle_message, args=(wx_inst,)).start()
    time.sleep(5)

    member_dict = {}

    # 这个是获取群具体成员信息的，成员结果信息也从上面的回调返回
    # wx_inst.get_member_of_chatroom('19442513534@chatroom')
    with open('wxidmerge.txt', encoding='utf-8') as f:
        print('open wxidmerge.txt')
        for line in f.readlines():
            member = line.split(',')
            member_name = member[0]
            member_wxid = member[1]
            member_dict[member_name] = member_wxid
            # print(member_name, member_wxid)
    print('read wxidmerge.txt finished')
    
    # wx_inst.send_img(to_user='23850395431@chatroom', img_abspath=r'D:\project\WechatPCAPI-new\1.png')

    # 这个是更新所有好友、群、公众号信息的，结果信息也从上面的回调返回
    # wx_inst.update_frinds()