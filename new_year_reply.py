# -*- coding: UTF-8 -*-

import threading
import itchat
import random
import os

replies = [
    '感谢您的元宵节祝福， 我也祝福你甜甜密密,团团圆圆,吃了汤圆,快乐过年!',
    '感谢您的元宵节祝福， 再美的日子如果没人牵挂也是种遗憾!也许祝福只是一种形式，但却能给心灵带来温馨，所以我们都把关心发给彼此，一样的感动，一样的祝福：元宵节快乐!'
    '感谢您的元宵节祝福， 在关爱中让友情更深，在牵挂中让亲情更暖，在诚实中让心底更静，在简单中让生活更美，在问候中让祝福更好，在祝福中让元宵节更快乐!',
    '感谢您的元宵节祝福， 我在这也希望你元宵节快乐：捂着肚子乐，蒙着被子乐，流着鼻涕乐，瞧着镜子乐，对天哈哈乐，喝水咕咕乐，想到我也乐，不乐也得乐，看你乐不乐，永远都快乐! ',
    '感谢您的元宵节祝福， 月儿圆圆，载着无尽的眷恋，春风渐渐，送去真挚的情感，愿元宵节夜晚，你潇洒美丽如愿，生活五彩斑斓，幸福与您相伴到永远!'
]
user = []
AUTO_SEND_TIME = 60

@itchat.msg_register(itchat.content.TEXT)
def newyear_reply(msg):
    receive = msg['Text']
    if '元宵' in receive or '月' in receive or '祝' in receive or '汤' in receive or '团员' in receive:
        n = random.randint(0, len(replies)-1)
        print(msg['User'])
        if msg['FromUserName'] in user:
            return
        else:
            user.append(msg['FromUserName'])
            return replies[n]

class ThreadJob(threading.Thread):
    def __init__(self, callback, event, interval):
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob, self).__init__()
        self._stop_event = threading.Event()
        self.is_running = False

    def run(self):
        self.is_running = True
        while not self.event.wait(self.interval):
            self.callback()
        self._stop_event = threading.Event()

    def stop(self):
        self.is_running = False
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def heartbeat():
    itchat.send('Heartbeat', 'filehelper')

k = ThreadJob(heartbeat, threading.Event(), AUTO_SEND_TIME)
if not k.is_running:
    k.start()

def main():
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()


