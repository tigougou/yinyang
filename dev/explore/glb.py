#! /usr/bin/python
# coding = utf-8
from util.dm import *

""" 本模块包括全局维护的全局变量 """




class Scene:
    def __init__(self,name,higherSceneDict,lowerSceneDict):
        self.higherSceneDict = higherSceneDict
        self.lowerSceneDict = lowerSceneDict
        self.name = name
    def fromYardToExplore(self):
        ret = find_pic_loop('global/tansuo.bmp|global/tansuo1.bmp', sim= 0.9, times= 1,success_image='global/tansuoqueren.bmp',offsetx=-738, offsety=-427)
        if(ret != ""):
            print('enter explore success!')


yard = Scene('yard',{},{"explore":Scene.fromYardToExplore})






