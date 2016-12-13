import threading,time
from explore.explore_function import *
from explore.glb import *
from util.dm import *
from bre.Break_yy_function import *
import multiprocessing
from multiprocessing import Manager,Value
from activity.activity_function import  *
import datetime
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication,QVBoxLayout,QHBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread
import os,sys
import psutil
from explore.log import *
'''
全局变量
'''
cur_power = 0
explore_mutex =  threading.Lock()
chapter_num = 17
difficulty_mode = 1
simulater_num = 2
explore_thread = None
medal = 4#奖牌数
"""
获取当前体力函数
Parameters:

Returns：
  成功：当前体力整形值
  失败：0
Raises:
"""
def get_cur_power():
    # 获取当前体力
    str = get_str(764,17,808,41,color="b@2a1909-101010",sim=0.9)
    if(str != ""):
        power = int(str)
        return power
    else:
        return 0
"""
获取当前突破票数函数
Parameters:

Returns：
  成功：当前突破票数
  失败：0
Raises:
"""
def get_cur_break_ticket():
    #获取当前结界突破票数
    str = get_str(989,16,1024,42,color="b@2a1909-101010",sim=0.9)
    if(str != ""):
        ticket = int(str)
        return ticket
    else:
        return 0
"""
好友任务处理线程

暂时设定为所有邀请都取消，后期需要添加判定

var:
"""
class friendTarget(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
    def run(self):
        #所有申请都点击取消
        bind(2)
        print("start friendTarget process")
        while(1):
            find_pic_loop('process/denial.bmp',offsetx=261,offsety=367,wait_delta=3)
            find_pic_loop('process/power_buy.bmp',offsetx=0,offsety=0,wait_delta=3)


"""
探索线程

在run函数中是一个无限循环，首先做一个窗口绑定，然后进行探索，探索后刷新体力值
探索流程：
1.到探索场景
2.进入全局变量的章节与难度对应的副本进行探索
3.出来后刷新当前体力值
var:
"""
class exploreThread(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        global chapter_num
        global cur_power
        global explore_mutex
        print("cur_power = " + str(cur_power))
        print('explore pid: ' + str(os.getpid()))

        bind(2)
        print("waiting explore start...")
        if explore_mutex.acquire():
            print("start exploring")
            #到探索场景
            print("change_scene('explore') need to be called")
            #调用探索函数，进入一次，结束后应该在探索场景中
            autoexplore(chapter=chapter_num, difficulty_mode=difficulty_mode)

            cur_power = get_cur_power()
            unbind_window()
            explore_mutex.release()
    def terminate(self):
        print('enter explore terminate')
        # ret = unbind_window()
        # if(ret == 1):
        #     print('unbind success')
        print('explore super terminate')
        super().terminate()
"""
阴阳寮突破进程

首先绑定窗口
突破流程：
var:
"""
class yyBreakThread(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
        #self.daemon = True
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        print("yy breakTread start...")

        bind(2)
        autobreak_yy(medal = medal)
        unbind_window()
"""
突破线程

暂时不能添加
突破流程：
var:
"""
class breakThread(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
        #self.daemon = True
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        print("waiting breakTread start...")
"""
任务分发主线程

暂时不能添加
突破流程：
var:
    explore_thread -当前正在进行的探索线程
    break_thread - 当前正在进行的突破线程
"""
class mainThread(QThread):
    def __init__(self):
        super().__init__()
        self.explore_thread = None
        self.yy_break_thread = None
        self.friend_target_thread = friendTarget()
        #self.break_thread = None
    def run(self):
        global cur_power
        global explore_mutex
        yaoguaituizhi_first = 1
        yaoguaituizhi_second = 1
        yaoguaituizhi_gift_first = 1
        yaoguaituizhi_gift_second = 1
        power_get_first = 1
        power_get_second = 1
        last_yy_break_time = datetime.datetime.now() - datetime.timedelta(seconds= 800)
        self.main_thread_window_bind()
        print('main thread pid: ' + str(os.getpid()))
        time.sleep(5)
        self.friend_target_thread.start()
        # 本线程应该无限循环进行各个任务的分发

        while(1):
            print('进入循环')


            #进入体力判定流程，首先进入探索界面
            #change_scene('explore')

            if(explore_mutex.acquire(timeout=30)):
                print('cur_time: ' + time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time())))
                cur_time = datetime.datetime.now()
                hour = int(time.strftime('%H',time.localtime(time.time())))
                minute = int(time.strftime('%M',time.localtime(time.time())))
                #活动时间判断

                if(hour == 12 and minute > 3 and power_get_first == 1):
                    change_scene('yard')
                    activity_power_get()
                    power_get_first = 0
                    change_scene('explore')
                if(hour == 22 and minute > 3 and power_get_second == 1):
                    change_scene('yard')
                    activity_power_get()
                    power_get_second = 0
                    change_scene('explore')
                #阴阳寮结界判定
                #时间间隔700s
                if((cur_time - last_yy_break_time).seconds > 700):
                    print("start yy break")
                    self.yy_break_thread = yyBreakThread()
                    time.sleep(5)
                    self.yy_break_thread.start()
                    self.yy_break_thread.join()
                    #等待结束
                    last_yy_break_time = datetime.datetime.now()
                print('start get power and ticket value')
                #change_scene('explore')
                cur_power = get_cur_power()
                cur_break_ticket = get_cur_break_ticket()
                print('cur_power: ' + str(cur_power))
                print('cur_ticket: ' + str(cur_break_ticket))
                if(cur_break_ticket >= 9):
                    print("start breaking")

                if cur_power >= 20:
                    #体力大于等于20，创建新的探索线程对象，开始线程
                    print("create explore_thread")
                    self.explore_thread = exploreThread()
                    print(os.getpid())
                    print(self.explore_thread)
                    self.explore_thread.daemon = False
                    self.explore_thread.start()
                    print('开启探索线程')
                    self.explore_thread.join()
                    explore_mutex.release()
                    continue
                #整个流程走完，释放锁
                explore_mutex.release()
            else:print("can't get lock,waiting.....")
            time.sleep(30)
    def terminate(self):
        global explore_mutex
        print('enter main_process terminate')
        self.main_thread_window_unbind()
        print('111')
        print(self.explore_thread)
        if(self.explore_thread != None):
            if(self.explore_thread.is_alive()):
                print('killing explore')
                self.explore_thread.terminate()
        if(self.yy_break_thread != None):
            if(self.yy_break_thread.is_alive()):
                print('killing yybreak')
                self.yy_break_thread.terminate()
        if(self.friend_target_thread != None):
            if(self.friend_target_thread.is_alive()):
                print('killing friend_target_thread')
                self.friend_target_thread.terminate()
        print('super terminate')
        super().terminate()


    def main_thread_window_bind(self):
        global simulater_num
        bind(2)
    def main_thread_window_unbind(self):
        ret = unbind_window()
        if(ret == 1):
            print('unbind success')



#图形化界面


"""
总体gui类
"""
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.main_thread = None


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('welcome to tigougou')
        #开始按钮
        self.startBtn = QPushButton('start')
        self.startBtn.setToolTip('开启主线程')
        self.startBtn.resize(self.startBtn.sizeHint())
        self.startBtn.clicked.connect(self.start_process)
        #暂停按钮
        self.pause_btn = QPushButton('pause')
        self.pause_btn.setToolTip('暂停全部线程')
        self.pause_btn.resize(self.pause_btn.sizeHint())
        self.pause_btn.clicked.connect(self.pause_process)
        #第一行
        hbox = QHBoxLayout()
        hbox.addWidget(self.startBtn)
        hbox.addWidget(self.pause_btn)
        hbox.addStretch(1)
        #整体布局
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('tigougou')
        self.show()
    def closeEvent(self, event):
        if(self.main_thread.isRunning()):
            print('kill main')
            try:
                self.main_thread.terminate()
            except Exception:
                explore_mutex.release()
                print('get main quit except')
            event.accept()
    #开启线程处理程序
    def start_process(self):
        global explore_mutex
        sender = self.sender()
        if(sender.text() == 'start'):
            print('main_thread start')
            if(not explore_mutex.acquire(0)):
                explore_mutex.release()
            else:
                explore_mutex.release()
            self.main_thread = mainThread()
            self.main_thread.start()
            sender.setText('stop')
        elif(sender.text() == 'stop'):
            #unbind_window()
            #print('unbind_success!')
            if(self.main_thread.isRunning()):
                print('kill main')
                try:
                    self.main_thread.terminate()
                except Exception:
                    explore_mutex.release()
                    print('get main quit except')
            sender.setText('start')

    #暂停线程处理程序
    def pause_process(self):
        sender = self.sender()
        print('sender is ' + sender.text())
        if(sender.text() == 'pause'):
            if(self.main_thread.explore_thread != None):
                if(self.main_thread.explore_thread.is_alive()):
                    print('进程暂停  进程编号 %s ' %(self.main_thread.explore_thread.pid))
                    p = psutil.Process(self.main_thread.explore_thread.pid)
                    p.suspend()
            if(self.main_thread.yy_break_thread != None):
                if(self.main_thread.yy_break_thread.is_alive()):
                    p = psutil.Process(self.main_thread.yy_break_thread.pid)
                    p.suspend()
            if(self.main_thread.friend_target_thread != None):
                if(self.main_thread.friend_target_thread.is_alive()):
                    p = psutil.Process(self.main_thread.friend_target_thread.pid)
                    p.suspend()
            self.main_thread.main_thread_window_unbind()
            sender.setText('continue')
        elif(sender.text() == 'continue'):
            if(self.main_thread.explore_thread != None):
                if(self.main_thread.explore_thread.is_alive()):
                    print('进程继续  进程编号 %s ' %(self.main_thread.explore_thread.pid))
                    p = psutil.Process(self.main_thread.explore_thread.pid)
                    p.resume()
            if(self.main_thread.yy_break_thread != None):
                if(self.main_thread.yy_break_thread.is_alive()):
                    p = psutil.Process(self.main_thread.yy_break_thread.pid)
                    p.resume()
            if(self.main_thread.friend_target_thread != None):
                if(self.main_thread.friend_target_thread.is_alive()):
                    p = psutil.Process(self.main_thread.friend_target_thread.pid)
                    p.resume()
            time.sleep(5)
            self.main_thread.main_thread_window_bind()
            sender.setText('pause')













if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    # explore_thread = exploreThread()
    # explore_thread.start()







