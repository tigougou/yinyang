#! /usr/bin/python
# coding = utf-8
from util.dm import *

""" 本模块包括全局维护的全局变量 """



global yard
class Scene:
    def __init__(self,name,higherSceneDict,lowerSceneDict):
        self.higherSceneDict = higherSceneDict
        self.lowerSceneDict = lowerSceneDict
        self.name = name
    def fromYardToExplore(self):
        ret = find_pic_loop('global/tansuo.bmp|global/tansuo1.bmp', sim= 0.9, times= 1,success_image='global/tansuoqueren.bmp',offsetx=-738, offsety=-427)
        if(ret != ""):
            print('enter explore success!')




#探索场景
#结界突破场景
#章节场景
"""
全局变量初始化函数
Parameters:

Returns:
  成功：1
  失败：0
Raises:
"""
def glb_init():
    # 庭院对象,无高层对象
    global yard
    yard = Scene('yard', {}, {"explore": Scene.fromYardToExplore})
    # 当前场景对象，进入游戏后，默认画面为庭院
    global cur_scene
    cur_scene = yard
glb_init()







