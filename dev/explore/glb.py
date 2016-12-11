#! /usr/bin/python
# coding = utf-8
from util.dm import *
from explore.explore_function import  *
""" 本模块包括全局维护的全局变量 """
global cur_scene
class Scene:
    global cur_scene
    global scene_dic
    scene_dic = {}
    def __init__(self,name,higherSceneDict,lowerSceneDict):
        self.higherSceneDict = higherSceneDict
        self.lowerSceneDict = lowerSceneDict
        self.name = name
    def fromYardToExplore(self):
        global cur_scene
        ret = find_pic_loop("glb/main2explore.bmp|glb/main2explore2.bmp|glb/main2explore3.bmp", sim= 0.7, times= 200,success_image='explore/exploreflag.bmp')
        if(ret != ""):
            print('enter explore success!')
            cur_scene = scene_dic['explore']
    def fromExploreToYard(self):
        global cur_scene
        ret = find_pic_loop("glb/explore2yard.bmp", times=200, sim=0.7,
                            success_image='glb/yardflag1.bmp|glb/yardflag2.bmp')
        if (ret != ""):
            print('enter yard success!')
            cur_scene = scene_dic['yard']
'''
添加场景流程：
首先定义一个全局变量：如global yard
然后再glb_init函数中进行初始化： 添加global yard 并进行定义 如yard = Scene('yard', "", {"explore": Scene.fromYardToExplore})
在glb_init函数中将名字写入scene_dic字典中：scene_dic[yard.name] = yard
添加scene类的对应函数def fromYardToExplore(self):
'''

#全局变量
#场景字典
global scene_dic
#院子
global yard
#探索场景
global explore
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
    global cur_scene
    global yard
    global explore
    global scene_dic
    yard = Scene('yard', "", {"explore": Scene.fromYardToExplore})
    scene_dic[yard.name] = yard
    explore = Scene('explore',{'yard':Scene.fromExploreToYard}, {} )
    scene_dic[explore.name] = explore
    # 当前场景对象，进入游戏后，默认画面为庭院
    cur_scene = explore
glb_init()




def change_scene(next_scene):
    global cur_scene
    global scene_dic
    #最多进行100次
    for i in range(100):
        #已经到指定场景
        print("cur_scen.name = "+ str(cur_scene.name))
        if cur_scene.name == next_scene:
            return 1
        #指定场景在下层
        elif next_scene in cur_scene.lowerSceneDict.keys():
            cur_scene.lowerSceneDict[next_scene](cur_scene)
        #已经到达最顶层，切顶层无指定层的记录
        elif cur_scene.higherSceneDict == "":
            return 0
        #向顶层走
        else:
            for higher_scene in cur_scene.higherSceneDict.keys():
                cur_scene.higherSceneDict[higher_scene](cur_scene)














