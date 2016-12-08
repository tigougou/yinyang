from explore.explore_function import *
from util.dm import *
from common.common import *
WindowBind(1)

#scene_chang_handle("explore/exploreflag.bmp","explore/main2explore.bmp",sim = 0.8,tryTimes = 2000)

#ret = find_pic_loop("explore/exploreflag2.bmp",sim = 0.8,times = 20)

#print(ret)
enter_explore(difficulty_mode = 0)
while(True):
    ret = find_pic_loop("explore/monster-0.bmp",click_en = 0, sim = 0.8,times = 10, wait_delta = 0.1)
    print("")
    if ret != "":
        find_monster(0)
        break
    ret = find_pic_loop("explore/monster-1.bmp", click_en=0, sim=0.8, times=10, wait_delta=0.1)
    if ret != "":
        find_monster(1)
    else :
        moveto(970, 542)
        left_click()
scene_chang_handle("explore/exploreoutconfirm.bmp", "explore/exploreout.bmp",tryTimes=30)
scene_chang_handle("explore/exploreflag.bmp", "exploreoutconfirm.bmp",tryTimes=30)