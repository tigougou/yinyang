""" 本模块包括所有阴阳寮突破的基本功能函数 """
from common.common import *
from bre.Break_yy_function import *
"""
个人结界突破进入函数
Parameters:

Returns：
  成功：1
  失败：0
Raises:
"""
def break_person_enter():
    """本函数在探索界面下使用"""
    scene_chang_handle("break/enterbreak_flag.bmp","break/enterbreak.bmp",delaytime = 1,tryTimes = 30)
    scene_chang_handle("break/enterbreak2.bmp","break/breakpersonflag.bmp",delaytime = 1,tryTimes = 30)
    #scene_chang_handle("break/refreshflag.bmp", "break/refresh.bmp", delaytime=1, tryTimes=30)
    ret = find_pic_loop("break/refresh.bmp",times=30)
    if(ret == ""):
        return 0
    ret = find_pic_loop("break/refreshconfirm.bmp",times=30)
    if ret == "":
        return 0
    ret = find_pic_loop("break/fight.bmp|break/fight1.bmp|break/fight2.bmp|break/fight3.bmp",  click_en=0, sim=0.6, times=10, wait_delta=0.1)
    if ret == "":
        moveto(1,1)
        left_click()
        return 2
    #scene_chang_handle("break/norefreshflag.bmp", "break/refreshconfirm.bmp", delaytime=1, tryTimes=30)
    return 1
"""
个人结界突破选择函数
从奖牌低到高攻打
Parameters:
       medal - 奖牌数
Returns：
  成功：1
  失败：0
Raises:
"""
def break_person_choose(medal = 0):
    for i in range(1,5):
        ret = find_pic_loop("break/medal0.bmp", times=1, wait_delta=0.1)
        if (ret =="")&(medal > 0):
            ret = find_pic_loop("break/medal1.bmp", times=1, wait_delta=0.1)
            if (ret =="")&(medal>1):
                ret = find_pic_loop("break/medal2.bmp", times=1, wait_delta=0.1)
                if (ret == "")&(medal >2):
                    ret = find_pic_loop("break/medal3.bmp", times=1, wait_delta=0.1)
                    if (ret == "")& (medal > 3):
                        ret = find_pic_loop("break/medal4.bmp", times=1, wait_delta=0.1)
                        if (ret == "") & (medal > 4):
                            ret = find_pic_loop("break/medal5.bmp", times=1, wait_delta=0.1)
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
    time.sleep(2)
    return ret
"""
个人结界突破选择函数
Parameters:
    number - 号  1 2 3
                 4 5 6
                 7 8 9
    medal - 奖牌数
Returns：
  成功：1
  失败：0
Raises:
"""
#def break_person_choose2(number = 1,medal = 0):






"""
自动个人结界突破函数
Parameters:
       以下情况退出结界突破
       奖牌数量
Returns：
  成功：1
  失败：0
Raises:

"""
def autobreak_personal(number = 3,medal = 3):
    win_number = 0
    ret = break_person_enter()
    for i in(0,number):
        ret = break_person_choose(medal=medal)
        if ret =="":break
        ret = break_yy_fight()
        if ret ==0:break
        else:win_number = win_number +1
        if win_number==3|win_number == 6| win_number == 9:
            click_until_pic("explore/fightend_win_giftopen.bmp")
            scene_chang_handle("break/enterbreak_flag.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                               tryTimes=2000)
    break_yy_out()