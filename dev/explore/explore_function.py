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
def chapter_choose(chapter = 16):
    """本函数调用前需要任务在探索场景下"""

    #需要滚动来选定章节

    chapter = "explore/chapter-" + str(chapter)+".bmp"
    print(chapter)
    scene_chang_handle("explore/exploreflag2.bmp", chapter, sim=1, tryTimes=20)
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
def enter_explore(chapter = 16 , difficulty_mode = 0):
    """ 本函数调用前需要人物在探索场景下 """
    # 根据章节号找到对应的章节并点击
    chapter_choose(chapter)
    # 选择对应难度并点击探索按钮进入
    if difficulty_mode == 0:
        scene_chang_handle("explore/normalflag.bmp", "explore/normal.bmp",sim = 1)
    else:
        scene_chang_handle("explore/normal.bmp","explore/normalflag.bmp",sim = 1 )
    # 进行进入成功判定
    scene_chang_handle("explore/exploreEnterflag.bmp", "explore/exploreEnter.bmp",sim = 1)
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
        scene_chang_handle("explore/fight_enterflag.bmp", "explore/monster-0.bmp", delaytime=0.1, sim=0.7, tryTimes=200)
    elif monster_type == 1:
        scene_chang_handle("explore/fight_enterflag.bmp", "explore/monster-1.bmp", delaytime=0.1, sim=0.8, tryTimes=200)
    #elif monster_type == 2:
        """"""
    #else :
    #准备
    scene_chang_handle("explore/fightreadyflag.bmp", "explore/fightready.bmp", delaytime=0.1, sim=0.8, tryTimes=200)
    #攻击优先级
    moveto(970, 270)
    left_click()
    # 进行攻击成功判断
    while(1):
        ret = find_pic_loop("explore/fightend_win.bmp", sim=0.8,click_en = 1, times=1, wait_delta=0.1)
        if ret !="":
            win_flag = 1
            scene_chang_handle("explore/fightend_win_gift1.bmp","explore/fightend_win.bmp", delaytime=0.01, sim=0.6, tryTimes=200)
            scene_chang_handle("explore/fightend_win_giftopen.bmp", "explore/fightend_win_gift1.bmp", delaytime=0.01, sim=0.6,tryTimes=200)
            scene_chang_handle("explore/exploreEnterflag.bmp","explore/fightend_win_giftopen.bmp", delaytime=0.1, sim=0.8, tryTimes=200)
            break
        ret = find_pic_loop("explore/fightend_fail.bmp", sim=0.8, click_en=1, times=1, wait_delta=0.1)
        if ret !="":
            win_flag = 0
            break


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











