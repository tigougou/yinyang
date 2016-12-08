from explore.explore_function import *
from util.dm import *
from common.common import *
WindowBind(1)

#autoexplore(chapter=17)
ret = find_pic_loop("explore/baoxiang.bmp", click_en=0, sim=0.8, times=20, wait_delta=0.1)
if ret != "":
    scene_chang_handle("explore/fightend_win_gift1.bmp", "explore/baoxiang.bmp", delaytime=0.01, sim=0.6,
                           tryTimes=200)
    scene_chang_handle("explore/fightend_win_giftopen.bmp", "explore/fightend_win_gift1.bmp", delaytime=0.01,
                           sim=0.6, tryTimes=2000)
    scene_chang_handle("explore/exploreflag.bmp.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                           tryTimes=2000)
