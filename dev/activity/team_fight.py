#本模块包含所有组队挑战的函数
from common.common import *

"""
进入组队函数
Parameters:

Returns:
  成功：1
  失败：0

Raises:
"""
def teamfight_enter():
    #本模块再yard界面使用
    scene_chang_handle("teamfight/juanzhouopen.bmp", "teamfight/juanzhouclose.bmp", delaytime=1, sim=0.8, tryTimes=30)
    scene_chang_handle("teamfight/teamenterflag.bmp", "teamfight/teamenter.bmp", delaytime=1, sim=0.8, tryTimes=30)

"""
进入妖气封印函数
Parameters:
  monster_type  - 怪物类型 0：经验妖怪
                           1：金币妖怪
                           2：鬼使黑
                           3：海坊主
                           4：椒图
                           5：跳跳哥哥
                           6：二口女
                           7：骨女
                           8：饿鬼
Returns:
  成功：1
  失败：0

Raises:
"""
def seal_enter(monster_type =2):
    scene_chang_handle("teamfight/sealenterflag.bmp", "teamfight/sealenter.bmp", delaytime=1, sim=0.8, tryTimes=30)
    while(1):
        while(1):
            if monster_type == 0:
                find_pic_loop("teamfight/jingyanyaoguai.bmp", click_en=1, offsetx=524, offsety=31,sim=0.8, times=10)
            elif monster_type ==1:
                find_pic_loop("teamfight/jinbiyaoguai.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==2:
                find_pic_loop("teamfight/guishihei.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==3:
                find_pic_loop("teamfight/haifangzhu.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==4:
                find_pic_loop("teamfight/jiaotu.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==5:
                find_pic_loop("teamfight/tiaotiaogege.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==6:
                find_pic_loop("teamfight/erkounv.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            elif monster_type ==7:
                find_pic_loop("teamfight/gunv.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            else:
                find_pic_loop("teamfight/egui.bmp", click_en=1, offsetx=524, offsety=31, sim=0.8, times=10)
            time.sleep(1)
            ret = find_pic_loop("teamfight/refresh.bmp", click_en=1, sim=0.8, times=20)
            if ret =="":break
        while(1):
            ret = find_pic_loop("teamfight/teamflag.bmp|explore/fightready.bmp", click_en=0, sim=0.8, times=1)
            if ret !="":
                ret = find_pic_loop("explore/fightready.bmp", click_en=0, sim=0.8, times=400)
                if ret != "":return 1

"""
进入妖气封印函数
Parameters:
  fight_type - 组队攻打类型 0：觉醒火
                           1：觉醒风
                           2：觉醒水
                           3：觉醒雷
                           4：御魂
                           5：妖气封印

  monster_type or leve  -
                   fight_type = 5时代表怪物类型
                           0：经验妖怪
                           1：金币妖怪
                           2：鬼使黑
                           3：海坊主
                           4：椒图
                           5：跳跳哥哥
                           6：二口女
                           7：骨女
                           8：饿鬼
                    fight_type = 0-4时为层数
Returns:
  成功：1
  失败：0

Raises:
"""
def autoteamfight(fight_type =5,monster_type_or_leve = 1):
    teamfight_enter()
    if fight_type ==5:
        seal_enter(monster_type = monster_type_or_leve)
    scene_chang_handle("explore/fightreadyflag.bmp", "explore/fightready.bmp|explore/fightready1.bmp", delaytime=0.1, sim=0.7, tryTimes=300)
    # 攻击优先级

    # 进行攻击成功判断
    while (1):
        ret = find_pic_loop("explore/fightend_win.bmp|teamfight/fightwinflag.bmp", sim=0.8, click_en=1, times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 1
            moveto(1, 1)
            click_until_pic("explore/fightend_win_giftopen.bmp")
            scene_chang_handle("teamfight/juanzhouopen.bmp", "explore/fightend_win_giftopen.bmp", delaytime=0.1,
                               tryTimes=2000)
            break
        ret = find_pic_loop("explore/fightend_fail.bmp", success_image="explore/exploreEnterflag.bmp", sim=0.8,
                            click_en=1, times=1, wait_delta=0.1)
        if ret != "":
            win_flag = 0
            break
    return 1