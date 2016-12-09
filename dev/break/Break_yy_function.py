from common.common import *
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
"""
阴阳寮结界选择函数
Parameters:
numeber - 阴阳寮序号

Returns：
成功：1
失败：0

Raises:
"""
def break_yy_choose( number = 0):
    """本函数在阴阳寮选择界面下使用"""
"""
阴阳寮结界突破 攻击对象选择函数
Parameters:
medal - 奖牌数量
level - 等级
Returns：
成功：1
失败：0

Raises:
"""
def break_yy_fightchoose( number = 0):
    """本函数在阴阳寮已选择界面下使用"""
"""
阴阳寮结界突破 攻击函数
Parameters:

Returns：
成功：1
失败：0

Raises:
"""
def break_yy_fight( number = 0):
    """本函数在阴阳寮攻击对象已选择界面下使用"""
"""
阴阳寮结界突破 自动突破函数
Parameters:

Returns：
成功：1
失败：0

Raises:
"""
def autobreak_yy( ):
    """本函数在阴阳寮攻击对象已选择界面下使用"""



