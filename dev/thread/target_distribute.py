import threading,time
explore_mutex =  threading.Lock()
class exploreThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if explore_mutex.acquire():
            print("exploring")
            #到探索场景
            #
            explore_mutex.release()

if __name__ == '__main__':
    hour = int(time.strftime('%H',time.localtime(time.time())))
    minite = int(time.strftime('%M', time.localtime(time.time())))
    if(hour == 13 and minite>10):
        yaoguaituizhi_en = 1
