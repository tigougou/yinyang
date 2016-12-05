from util.dm import *
import time

def bind(simulater):
    WindowBind(simulater)
def log():
    # 根据博远雅裤子的图片的相对位移来点击进入游戏
    find_pic_loop(r"log/jinruyouxi.bmp",click_en=1, offsetx=399, offsety=151, wait_delta=1, times=180)



bind(2)
while(True):
    log()
    time.sleep(5)