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

    #判断当前章节，没有的话从头扫到尾

    chapter = "explore/chapter-" + str(chapter)+".bmp"
    scene_chang_handle("explore/exploreflag2.bmp", chapter, sim=0.6, tryTimes=20)
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
def enter_explore(chapter = 17, difficulty_mode = 0):
    """ 本函数调用前需要人物在探索场景下 """
    # 根据章节号找到对应的章节并点击
    chapter_choose(chapter)
    # 选择对应难度并点击探索按钮进入
    if difficulty_mode == 0:
        scene_chang_handle("explore/normalflag.bmp", "explore/normal.bmp",sim = 0.8)
    else:
        scene_chang_handle("explore/normal.bmp","explore/normalflag.bmp",sim = 0.7 )
    # 进行进入成功判定
    scene_chang_handle("explore/exploreEnterflag.bmp", "explore/exploreEnter.bmp",sim = 0.7)
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
    # 根据怪物类型设定查找集合

    # 进行查找并点击攻击（需要合适的算法进行找怪）

    # 进行攻击成功判断

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











