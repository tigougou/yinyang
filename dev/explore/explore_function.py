#! /usr/bin/python
# coding = utf-8

""" 本模块包括所有探索基本功能函数 """

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
def enter_explore(chapter, difficulty_mode):
    """ 本函数调用前需要人物在探索场景下 """
    # 根据章节号找到对应的章节并点击

    # 选择对应难度并点击探索按钮进入

    # 进行进入成功判定

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











