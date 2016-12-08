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
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
)