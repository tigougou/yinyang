#! /usr/bin/python
# coding = utf-8
import util.dm as utdm
import time
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
场景切换功能函数
Parameters:
  state_next - 下一个场景标志路径
  pic_click - 进入下一个场景要点击的图片
  timeout - 切换场景超时时间(单位：s)最小0.01
Returns:
  成功：1
  失败：0
Raises:
"""
def scene_chang_handle(state_next,pic_click,timeout = 2):
    timeout = timeout * 100
    for  i in range(1,timeout):
        utdm.find_pic_loop(pic_click)
        ret = utdm.find_pic_loop(state_next,click_en = 0)
        if ret == 1:
            return 1
    return 0

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