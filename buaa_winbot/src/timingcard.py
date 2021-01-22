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
from datetime import datetime


logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    print(message)
    queue_recved_message.put(message)


# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    while True:
        message = queue_recved_message.get()
        print(message)


def main():
        wx_inst = WechatPCAPI(on_message=on_message, log=logging)
        wx_inst.start_wechat(block=True)

        while not wx_inst.get_myself():
            time.sleep(5)

     
        print('登陆成功')
        print(wx_inst.get_myself())

        threading.Thread(target=thread_handle_message, args=(wx_inst,)).start()

        # filehelper

        # 每天00：01 08:00 18:00定时发送 19442513534@chatroom  班级群

        # 新增@群里的某人的功能
        # wx_inst.send_text(to_user='13687903946@chatroom', msg='等我来5杀, and @ you', at_someone='wxid_fr8dgerdn87221')

        while True:
            current_time = datetime.now().strftime('%H:%M')
            print("now_time: {}".format(current_time))
            if current_time in ["00:15", "08:00", "18:00"]:
                wx_inst.send_img(to_user='filehelper', img_abspath=r'D:\project\WechatPCAPI-new\sc.png')
                wx_inst.send_text(to_user='filehelper', msg='长按图片进入北航小程序，点击信息填报，记得每日打卡，祝假期愉快哟')
                time.sleep(60)
            else:
                time.sleep(60)


if __name__ == '__main__':
    main()
