from common.common import *
from util.dm import *
""" 本模块包括所有阴阳寮突破的基本功能函数 """

"""
阴阳寮结界突破进入函数
Parameters:

Returns：
  成功：1
  失败：0
Raises:
"""
def break_yy_enter():
    """本函数在探索界面下使用"""
    #本函数运行到阴阳寮选择界面"""
    scene_chang_handle("break/enterbreak_flag.bmp","break/enterbreak.bmp",delaytime = 1,tryTimes = 30)
    scene_chang_handle("break/enterbreak_flag2.bmp","break/enterbreak2.bmp",delaytime = 1,tryTimes = 30)
"""
阴阳寮结界突破状态判断函数
Parameters:

Returns：
  未开启：0
  已开启：1
Raises:
"""
def break_yy_judge():
    """本函数在阴阳寮选择界面下使用"""
    ret = find_pic_loop("break/breakopenflag.bmp|break/breakopenflag1.bmp",times=10, click_en = 0)
    if ret =="":
        return 0
    else:
        return 1
"""
阴阳寮结界选择函数
Parameters:
numeber - 阴阳寮序号 1.2.3

Returns：
成功：1
失败：0

Raises:
"""
def break_yy_choose( number = 1):
    """本函数在阴阳寮选择界面下使用"""
    if number == 1:
        while(1):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=149,times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=100, y1=158, x2=175, y2=269,sim=0.8, times=20, click_en=0)
            if ret != "":break
    elif number == 2:
        while(1):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=220, times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=100, y1=372, x2=175, y2=444,sim=0.8, times=20, click_en=0)
            if ret !="":break
    else:
        while(1):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=400, times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=100, y1=561, x2=175, y2=621,sim=0.8, times=20, click_en=0)
            if ret !="":break
    #left_click()
"""
阴阳寮结界突破 攻击对象选择函数
Parameters:
medal - 奖牌数量
level - 等级
Returns：
成功：1
失败：0
当前阴阳寮不能攻击：2
Raises:
"""
def break_yy_fightchoose( medal = 0,level = 0):
    """本函数在阴阳寮已选择界面下使用"""
    #判断奖牌数量
    while (1):
        if medal ==0:
            ret =find_pic_loop("break/medal0.bmp",times=5, wait_delta=0.1, sim=0.8)
        elif medal == 1:
            ret =find_pic_loop("break/medal1.bmp", times=5, wait_delta=0.1, sim=0.8)
        elif medal == 2:
            ret =find_pic_loop("break/medal2.bmp", times=5, wait_delta=0.1, sim=0.8)
        elif medal == 3:
            ret =find_pic_loop("break/medal3.bmp", times=5, wait_delta=0.1, sim=0.8)
        elif medal == 4:
            ret =find_pic_loop("break/medal4.bmp", times=5, wait_delta=0.1, sim=0.8)
        elif medal == 5:
            ret =find_pic_loop("break/medal5.bmp|break/medal4.bmp", times=5, wait_delta=0.1, sim=0.8)
        else:
            return 0
        if ret != "":break
        else:
            ret = find_pic_loop("break/p_chooseflag.bmp", times=5, sim = 0.8,wait_delta=0.1,click_en = 0)
        #未找到 翻页
        ret = find_pic_loop("break/medal0.bmp|break/medal1.bmp|break/medal2.bmp|break/medal3.bmp|break/medal4.bmp|break/medal5.bmp", click_en = 0,times=5, wait_delta=0.1,sim = 0.8)
        if ret == "":
            return 0
        else:
            moveto(575, 239)
            whelldown()
   #判断等级（根据奖牌数量的坐标寻找）

    ret = find_pic_loop("break/fight.bmp|break/fight1.bmp|break/fight2.bmp",  click_en=0, sim=0.8, times=10, wait_delta=0.1)
    if ret == "":
        moveto(1,1)
        left_click()
        return 2
"""
阴阳寮结界突破 攻击函数
Parameters:

Returns：
成功：1
失败：0

Raises:
"""
def break_yy_fight():
    """本函数在阴阳寮攻击对象已选择界面下使用"""

    #点击攻击按钮
    scene_chang_handle("explore/fightready.bmp","break/fight.bmp|break/fight.bmp",delaytime=1, sim=0.6, tryTimes=30)
    #等待准备
    scene_chang_handle("break/fightreadyflag.bmp", "explore/fightready.bmp", delaytime=0.1, sim=0.7, tryTimes=200)
    #攻击优先级
    #moveto(970, 270)
    #left_click()
    while (1):
        ret = find_pic_loop("explore/fightend_win.bmp", sim=0.8, times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 1
            # scene_chang_handle("explore/fightend_win_gift1.bmp","explore/fightend_win.bmp", delaytime=0.01, sim=0.6, tryTimes=2000)
            click_until_pic("explore/fightend_win_giftopen.bmp")
            scene_chang_handle("explore/fightend_win_giftopen.bmp", "explore/fightend_win_gift1.bmp", delaytime=0.01,
                               sim=0.6, tryTimes=2000)
            scene_chang_handle("break/enterbreak_flag.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                               tryTimes=2000)
            break
        ret = find_pic_loop("explore/fightend_fail.bmp", success_image = "break/enterbreak_flag.bmp",sim = 0.8,times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 0
            break
    return 1

"""
阴阳寮退出 功能函数
Parameters:

Returns：
成功：1
失败：0
"""
def break_yy_out():
    scene_chang_handle("break/enterbreak.bmp", "break/breakout.bmp", delaytime=0.1,tryTimes=2000)

""""""""""
阴阳寮结界突破 自动突破函数
Parameters:

Returns：
成功：1
失败：0

Raises:
"""
def autobreak_yy(medal = 0):
    break_yy_enter()
    for i in {1, 2, 3}:
        ret = break_yy_judge()
        if ret == 0:
            break
        break_yy_choose(number=i)
        ret = break_yy_fightchoose(medal = medal)
        if ret == 0:
            print("nothing to do")
        elif ret != 2:
            break_yy_fight()
    break_yy_out()
    """本函数在阴阳寮攻击对象已选择界面下使用"""



