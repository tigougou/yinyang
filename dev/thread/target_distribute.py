import threading,time
from explore.explore_function import *
from explore.glb import *
from util.dm import *
from explore.log import *
explore_mutex =  threading.Lock()
chapter_num = 17
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
class exploreThread(threading.Thread):
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        global chapter_num
        print("waiting explore start...")
        if explore_mutex.acquire():
            print("start exploring")
            #到探索场景
            print("change_scene('explore') need to be called")
            #调用探索函数，进入一次，结束后应该在探索场景中
            autoexplore(chapter=chapter_num, difficulty_mode=1)
            explore_mutex.release()
class breakThread(threading.Thread):
    def run(self):
        #首先判定锁是否被占用，若占用则堵塞，等待锁的释放
        global chapter_num
        print("waiting breakTread start...")
        if explore_mutex.acquire():
            print("start exploring")
            #到探索场景
            print("change_scene('explore') need to be called")
            #调用探索函数，进入一次，结束后应该在探索场景中
            autoexplore(chapter=chapter_num, difficulty_mode=1)
            explore_mutex.release()
if __name__ == '__main__':

    explore_thread = exploreThread()
    break_thread = breakThread()
    yaoguaituizhi_first = 0
    yaoguaituizhi_baoxiang_first = 0
    yaoguaituizhi_en = 0
    yaoguaituizhi_baoxiang_en = 0
    bind(2)
    while(True):
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
            explore_thread.join()







