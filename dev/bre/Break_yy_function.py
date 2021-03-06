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
  可攻打的阴阳寮个数
Raises:
"""
def break_yy_judge():
    """本函数在阴阳寮选择界面下使用"""
    ret = find_pic_loop("break/weigongda2.bmp",times=10, click_en = 0, sim=0.8)
    if ret =="":return 3
    ret = ret.split('|')
    ret = len(ret)
    ret = 3 - ret
    return ret
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
        for i in range(50):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=149,times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=122, y1=247, x2=159, y2=291,sim=0.8, times=20, click_en=0)
            if ret != "":break
        if(ret == ""): return 0
    elif number == 2:
        for i in range(50):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=315, times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=122, y1=430, x2=159, y2=470,sim=0.8, times=20, click_en=0)
            if ret !="":break
        if(ret == ""): return 0
    else:
        for i in range(50):
            find_pic_loop("break/enterbreak_flag.bmp", offsetx=-382, offsety=564, times=30, wait_delta=0.1)
            ret = find_pic_loop("break/yylchooseflag1.bmp|break/yylchooseflag2.bmp", x1=122, y1=617, x2=151, y2=657,sim=0.8, times=20, click_en=0)
            if ret !="":break
        if(ret == ""): return 0
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
    medal = int(medal)
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
            ret =find_pic_loop("break/medal4.bmp|break/medal5.bmp", times=5, wait_delta=0.1, sim=0.8, mode=3)
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
            moveto(820, 280)
            left_down()
            time.sleep(0.1)
            moveto(820, 200)
            time.sleep(0.1)
            moveto(820, 120)
            left_up()
            time.sleep(2)
   #判断等级（根据奖牌数量的坐标寻找）
    time.sleep(2)
    ret = find_pic_loop("break/fight.bmp|break/fight1.bmp|break/fight2.bmp|break/fight3.bmp",  click_en=0, sim=0.7, times=10, wait_delta=0.1)
    if ret == "":
        moveto(1,1)
        left_click()
        return 2
    else:return 1
"""
阴阳寮结界突破 攻击函数
Parameters:

Returns：
成功：1
失败：0
准备超时：2
Raises:
"""
def break_yy_fight():
    """本函数在阴阳寮攻击对象已选择界面下使用"""

    #点击攻击按钮
    ret = scene_chang_handle("explore/fightready.bmp","break/fight1.bmp|break/fight2.bmp|break/fight3.bmp",delaytime=1, sim=0.7, tryTimes=50)
    if ret ==0:return 2
    #等待准备
    scene_chang_handle("break/fightreadyflag1.bmp", "explore/fightready.bmp|explore/fightready1.bmp", delaytime=0.1, sim=0.6, tryTimes=200)
    #攻击优先级
    #moveto(970, 270)
    #left_click()
    while (1):
        ret = find_pic_loop("explore/fightend_win.bmp", sim=0.8, times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 1
            # scene_chang_handle("explore/fightend_win_gift1.bmp","explore/fightend_win.bmp", delaytime=0.01, sim=0.6, tryTimes=2000)
            click_until_pic("explore/fightend_win_giftopen.bmp")
            scene_chang_handle("break/enterbreak_flag.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                               tryTimes=2000)
            break
        ret = find_pic_loop("explore/fightend_fail.bmp", success_image = "break/enterbreak_flag.bmp",sim = 0.8,times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 0
            break
    return win_flag

"""
阴阳寮退出 功能函数
Parameters:

Returns：
成功：1
失败：0
"""
def break_yy_out():
    scene_chang_handle("break/enterbreak.bmp", "break/breakout.bmp", delaytime=0.1,tryTimes=2000, sim=0.8)

""""""""""
阴阳寮结界突破 自动突破函数
Parameters:

Returns：
成功：1
失败：0

Raises:
"""
def autobreak_yy(medal = 0):
    cnt = 0
    failed_to_find_num = 0
    break_yy_enter()
    a = break_yy_judge()
    for i in range(1,a+1):
        break_yy_choose(number=i)
        ret = break_yy_fightchoose(medal = medal)
        if ret == 0:
            failed_to_find_num += 1
            print("nothing to do")
        elif ret == 1:
            ret = break_yy_fight()
            if ret == 1:
                cnt += 1
            if ret ==2:
                moveto(1, 1)
                left_click()


    if(failed_to_find_num > 0 and medal != 5):
        #由于存在寮内未找到对手，将奖牌数提升至最高再找一遍
        medal = 5
        break_yy_enter()
        a = break_yy_judge()
        for i in range(1,a+1):
            break_yy_choose(number=i)
            ret = break_yy_fightchoose(medal = medal)
            if ret == 0:
                print("nothing to do")
            elif ret != 2:
                ret = break_yy_fight()
                if ret == 1:
                    cnt += 1
    break_yy_out()
    return cnt
    """本函数在阴阳寮攻击对象已选择界面下使用"""



