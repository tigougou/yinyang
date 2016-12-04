#! /usr/bin/python
# coding = utf-8

""" 本模块包括所有通用基本功能函数及通用全局变量 """
'''
全局状态字典
Parameters:
  secen  - 当前处于的场景
  physicalPower - 体力值
'''
status_dic = { "secen":"",
               "physicalPower": 0 }


"""
回合开始处理功能函数
Parameters:
  mode  - 模式 0：探索副本，突破副本等
  prepare_flag - 是否准备flag
Returns:
  成功：1
  失败：0
Raises:
"""
def round_start_handle(mode, prepare_flag):
    """ 本函数调用必须在回合开始环境下 """
    # 根据模式进行判定对应动作

"""
胜利处理功能函数
Parameters:
  mode  - 模式 0：探索副本，突破副本等
Returns:
  成功：1
  失败：0
Raises:
"""
def round_start_handle(mode, prepare_flag):
    """ 本函数调用必须在回合开始环境下 """
    # 根据模式进行判定对应动作