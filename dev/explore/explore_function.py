#! /usr/bin/python
# coding = utf-8
from common.common import *


""" 本模块包括所有探索基本功能函数 """


"""
章节选择功能函数
Parameters:
 chapter - 章节数 0-18
Returns：
  成功：1
  失败：0
Raises:
"""
def chapter_choose(chapter = 17):
    """本函数调用前需要任务在探索场景下"""
    #需要滚动来选定章节
    chapter = "explore/chapter-" + str(chapter)+".bmp"
    ret = find_pic_loop(chapter, click_en=0,sim=0.8, times=5)
    if ret !="":
        scene_chang_handle("explore/exploreflag2.bmp", chapter, tryTimes=20)
        return 1
    else:
        for i in range(0,30):
            time.sleep(0.3)
            moveto(1172,210)
            left_down()
            time.sleep(0.1)
            moveto(1172, 290)
            time.sleep(0.1)
            moveto(1172, 370)
            left_up()
            ret = find_pic_loop("explore/chapter-1.bmp", click_en=0, sim=0.8, times=7)
            if ret != "":
                break
            ret = find_pic_loop(chapter, click_en=0, sim=0.8, times=5)
            if ret != "":
                break
        for i in range(0,30):
            ret = find_pic_loop(chapter, click_en=0, sim=0.8, times=10)
            if ret !="":
                scene_chang_handle("explore/exploreflag2.bmp", chapter,sim=0.7, tryTimes=30)
                return 1
            moveto(1172, 370)
            left_down()
            time.sleep(0.1)
            moveto(1172, 290)
            time.sleep(0.1)
            moveto(1172, 210)
            left_up()
            time.sleep(0.3)
        return 0

""""""
"""
进入探索副本功能函数
Parameters:
  chapter  - 章节数 0-18
  difficulty_mode - 副本难度 0-1（简单，困难）
Returns:
  成功：1
  失败：0
Raises:
"""
def enter_explore(chapter = 17 , difficulty_mode = 0):
    """ 本函数调用前需要人物在探索场景下 """
    # 根据章节号找到对应的章节并点击
    chapter_choose(chapter)
    #判断是否在式神挑战状态


    # 选择对应难度并点击探索按钮进入
    if difficulty_mode == 0:
        scene_chang_handle("explore/normalflag.bmp", "explore/normal.bmp")
    else:
        scene_chang_handle("explore/normal.bmp","explore/normalflag.bmp")
    # 进行进入成功判定
    scene_chang_handle("explore/exploreEnterflag.bmp", "explore/exploreEnter.bmp")
"""
找怪功能函数
Parameters:
  monster_type  - 怪物类型 4bit标志 分别代表 经验怪，金币怪，御魂怪，boss怪
Returns:
  成功：1
  失败：0

Raises:
"""
def find_monster(monster_type):
    """ 本函数调用前需要人物在章节探索环境下 """
    # 根据怪物类型设定查找集合# 进行查找并点击攻击（需要合适的算法进行找怪）
    if monster_type == 0:
        ret = scene_chang_handle("explore/fight_enterflag.bmp", "explore/monster-0.bmp", delaytime=0.1, sim=0.7, tryTimes=40)
    elif monster_type == 1:
        ret = scene_chang_handle("explore/fight_enterflag.bmp", "explore/monster-1.bmp", delaytime=0.1, sim=0.7, tryTimes=40)
    #elif monster_type == 2:
        """"""
    #else :
    #准备
    if ret == 0:
        return 0
    scene_chang_handle("explore/fightreadyflag.bmp", "explore/fightready.bmp|explore/fightready1.bmp", delaytime=0.1, sim=0.7, tryTimes=200)
    #攻击优先级
    moveto(970, 270)
    left_click()
    # 进行攻击成功判断
    while(1):
        ret = find_pic_loop("explore/fightend_win.bmp", sim=0.7,click_en = 1, times=1, wait_delta=0.1)
        if ret !="":
            win_flag = 1
            #scene_chang_handle("explore/fightend_win_gift1.bmp","explore/fightend_win.bmp", delaytime=0.01, sim=0.6, tryTimes=2000)
            moveto(1,1)
            click_until_pic("explore/fightend_win_giftopen.bmp")
            #scene_chang_handle("explore/fightend_win_giftopen.bmp", "explore/fightend_win_gift1.bmp", delaytime=0.01, sim=0.6,tryTimes=2000)
            scene_chang_handle("explore/exploreEnterflag.bmp","explore/fightend_win_giftopen.bmp", delaytime=0.1, tryTimes=2000)
            break
        ret = find_pic_loop("explore/fightend_fail.bmp", success_image = "explore/exploreEnterflag.bmp", sim=0.7, click_en=1, times=1, wait_delta=0.1)
        if ret !="":
            win_flag = 0
            break
    return 1

"""
更换狗粮功能函数
Parameters:
Returns:
  成功：1
  失败：0
Raises:
"""
def change_dog_food():
    """ 本函数调用前需要在回合开始前的环境下 """
    # 查看换狗粮标志是否置位，若置位则查看是否有满级狗粮

    #若有满级狗粮，进行更换

    #进行换狗粮成功判断

"""
自动探索函数
Parameters:
    chapter - 章节数
    difficulty_mode - 难易程度 0 普通 ；1 困难
Returns:
  成功：1
  失败：0
Raises:
"""
def autoexplore(chapter,difficulty_mode = 0):
    enter_explore(chapter = chapter,difficulty_mode=difficulty_mode)
    while (True):
        ret = find_pic_loop("explore/monster-0.bmp|explore/monster-1.bmp", click_en=0, sim=0.8, times=15, wait_delta=0.1)
        if(ret != ""):
            print("找到可以攻击的怪物")
            ret = ret.split('|')
            monster_num = int(ret[0].split(',')[0])
            if(monster_num == 0):
                print("finding boss")
                #boss
                find_monster(0)
                break
            elif(monster_num == 1):
                print("")
                find_monster(1)
        else:
            time.sleep(0.5)
            moveto(970, 592)
            left_click()
    scene_chang_handle("explore/exploreoutconfirm.bmp", "explore/exploreout.bmp", tryTimes=30)
    scene_chang_handle("explore/exploreflag.bmp", "explore/exploreoutconfirm.bmp",tryTimes=30)
    #退出到探索页面 搜索宝箱
    ret = find_pic_loop("explore/baoxiang.bmp|explore/baoxiang1.bmp", click_en=0, sim=0.8, times=20, wait_delta=0.1)
    if ret != "":
        while(1):
            find_pic_loop("explore/baoxiang.bmp|explore/baoxiang1.bmp", click_en=1, sim=0.8, times=20, wait_delta=0.1)
            ret = find_pic_loop("explore/baoxiang.bmp|explore/baoxiang1.bmp", click_en=0, sim=0.8, times=20, wait_delta=0.1)
            if ret =="":break
        moveto(1,1)
        click_until_pic("explore/fightend_win_giftopen.bmp")
        scene_chang_handle("explore/exploreflag.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                           tryTimes=2000)
    return 1







