from util.dm import *
class Scene:
    def __init__(self,name,higherSceneList,lowerSceneList):
        self.higherSceneList = higherSceneList
        self.lowerSceneList = lowerSceneList
        self.name = name
    def fromYardToExplore(self):
        ret = find_pic_loop('global/tansuo.bmp|global/tansuo1.bmp', sim= 0.9, times= 1,success_image='global/tansuoqueren.bmp',offsetx=-738, offsety=-427)
        if(ret != ""):
            print('enter explore success!')





