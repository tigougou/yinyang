from explore.explore_function import *
from util.dm import *
from explore.glb import *
from bre.Break_yy_function import *
from thread.target_distribute import *

#WindowBind(1)
#autoexplore(chapter = 17)
#glb_init()
#print(explore.higherSceneDict)
#change_scene("explore")
#change_scene("yard")
#break_yy_enter()

#autobreak_yy()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
