import threading,time
from explore.explore_function import *
from explore.glb import *
from util.dm import *
import multiprocessing
import os
import psutil
from explore.log import *
def get_cur_power():
    # 获取当前体力
    str = get_str(764,17,808,41,color="b@2a1909-101010",sim=0.9)
    if(str != ""):
        power = int(str)
        return power
    else:
        return None
def get_cur_break_ticket():
    #获取当前结界突破票数
    str = get_str(989,16,1024,42,color="b@2a1909-101010",sim=0.9)
    if(str != ""):
        ticket = int(str)
        return ticket
    else:
        return None
class friendTarget(multiprocessing.Process):
    def run(self):
        #所有申请都点击取消
        print("start friendTarget process")
class exploreThread(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        global chapter_num
        while(True):
            print("waiting explore start...")
            if explore_mutex.acquire():
                cur_power = get_cur_power()
                if cur_power <= 20:
                    #此处开始探索线程
                    explore_mutex.release()
                    continue
                print("start exploring")
                #到探索场景
                print("change_scene('explore') need to be called")
                #调用探索函数，进入一次，结束后应该在探索场景中
                bind(2)
                autoexplore(chapter=chapter_num, difficulty_mode=1)
                explore_mutex.release()
class breakThread(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pid = os.getpid()
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        print("waiting breakTread start...")
        if explore_mutex.acquire():
            explore_mutex.release()



explore_mutex =  threading.Lock()
chapter_num = 17




#-----------------gui------------------------------
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.explore_thread = exploreThread()
        self.break_thread = breakThread()
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('start', self)
        btn.setToolTip('开启主线程')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.start_process)
        btn.move(50, 50)

        pause_btn = QPushButton('pause', self)
        pause_btn.setToolTip('暂停全部线程')
        pause_btn.resize(btn.sizeHint())
        pause_btn.clicked.connect(self.pause_process)
        pause_btn.move(150, 50)



        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()
    def start_process(self):
        sender = self.sender()
        if(sender.text() == 'start'):
            self.explore_thread = exploreThread()
            self.break_thread = breakThread()
            self.main_process(self.explore_thread, self.break_thread)
            sender.setText('stop')
        elif(sender.text() == 'stop'):
            if(self.explore_thread.is_alive()):
                self.explore_thread.terminate()
            unbind_window()
            sender.setText('start')

    def pause_process(self):
        sender = self.sender()
        print('sender is ' + sender.text())
        if(sender.text() == 'pause'):
            if(self.explore_thread.is_alive()):
                print('进程暂停  进程编号 %s ' %(self.explore_thread.pid))
                p = psutil.Process(self.explore_thread.pid)
                p.suspend()
                unbind_window()
            sender.setText('continue')
        elif(sender.text() == 'continue'):
            if(self.explore_thread.is_alive()):
                print('进程继续  进程编号 %s ' %(self.explore_thread.pid))
                p = psutil.Process(self.explore_thread.pid)
                p.resume()
                bind(2)
            sender.setText('pause')
    def main_process(self,explore_thread,break_thread):
        yaoguaituizhi_first = 0
        yaoguaituizhi_baoxiang_first = 0
        yaoguaituizhi_en = 0
        yaoguaituizhi_baoxiang_en = 0


        bind(2)
        hour = int(time.strftime('%H',time.localtime(time.time())))
        minute = int(time.strftime('%M', time.localtime(time.time())))
        print("current time is " + str(hour) +":"+ str(minute))
        #------------------定点活动------------------
        #妖怪退治在13:00 - 13:30之间
        if(hour == 13 and minute>10):
            yaoguaituizhi_en = 1
        #妖怪退治宝箱在13:30 - 14：00之间
        elif(hour == 13 and minute > 40):
            yaoguaituizhi_baoxiang_en = 1
        #...鬼王，领体力等
        #---------------------------------------------
        if yaoguaituizhi_en == 1 and yaoguaituizhi_first != 1:
            #change_scene("yaoguaituizhi")
            #autoyaoguaituizhi()
            yaoguaituizhi_first = 1
        elif yaoguaituizhi_baoxiang_en == 1 & yaoguaituizhi_baoxiang_first != 1 :
            #change_scene("yaoguaituizhi")
            #autoyaoguaituizhi_baoxiang()
            yaoguaituizhi_baoxiang_first = 1
        #...其他情况
        #在上述使能均关闭时，进行探索或结界判定
        #change_scene('explore')
        cur_power = get_cur_power()
        cur_break_ticket = get_cur_break_ticket()
        print("current power ： %d" % cur_power )
        print("current break_ticket ： %d" % cur_break_ticket )
        if cur_break_ticket >= 9:
            #此处跑一波结界突破
            print("break run...")
            print("break runover")
            #break_thread.start()
        if cur_power >= 20:
            #此处开始探索线程
            explore_thread.start()













if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    # explore_thread = exploreThread()
    # explore_thread.start()








