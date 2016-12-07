from util.dm import *
from explore.glb import *
import time

def bind(simulater):
    return WindowBind(simulater)
def log(hwnd,account = "",password = "",region = 0):
    #切换大区
    #find = find_pic_loop(r"log/qiehuan.bmp", click_en=1,offsetx=332, offsety=-2, wait_delta=1, times=5)
    if(account != ""):
        find = find_pic_loop(r"log/yonghuzhongxin.bmp", click_en=1, wait_delta=1, times=5)
        #之前无登陆记录的情况
        if(find != ""):
            # 有登陆记录的情况
            find = find_pic_loop(r"log/qiehuanzhanghao.bmp", click_en=1, wait_delta=1, times=5)
            if(find != ""):
                find = find_pic_loop(r"log/qitazhanghao.bmp", click_en=1, wait_delta=1, times=5)
            else:
                find = find_pic_loop(r"log/qitazhanghao.bmp", click_en=1, wait_delta=1, times=5)
        find_pic_loop(r"log/wangyiyouxiang.bmp", click_en=1, wait_delta=1, times=5)
        # 点击账号输入
        find_pic_loop(r"log/wangyiyouxi.bmp", click_en=1, offsetx=187, offsety=-32, wait_delta=1, times=5)
        send_string(hwnd, account)
        time.sleep(1)
        find_pic_loop(r"log/wangyiyouxi.bmp", click_en=1, wait_delta=1, times=5)
        time.sleep(1)
        # find_pic_loop(r"log/wangyiyouxi.bmp", click_en=1, wait_delta=1, offsetx=187, offsety=20, times=5)
        # 点击密码输入
        find_pic_loop(r"log/wangyiyouxi.bmp", click_en=1, offsetx=197, offsety=21, wait_delta=1, times=5)
        find = find_pic_loop(r"log/shanchumima.bmp", click_en=1, wait_delta=1, times=3)
        time.sleep(1)
        send_string(hwnd, password)
        time.sleep(1)
        find = find_pic_loop(r"log/denglu.bmp", click_en=1, wait_delta=1, times=5)
        if(find == 0):
            #登陆失败
            print("log failed")
            return 0
        else:
            #登录成功
            # 根据博远雅裤子的图片的相对位移来点击进入游戏
            find_pic_loop(r"log/jinruyouxi.bmp",click_en=1, offsetx=399, offsety=151, wait_delta=1,success_image="log/dianjijinru.bmp|log/jieshou.bmp", times=5,sim = 0.9)
            find_pic_loop(r"log/jieshou.bmp", click_en=1, offsetx=399, offsety=151, wait_delta=1, times=1)
            find_pic_loop(r"log/dianjijinru.bmp", click_en=1, offsetx=399, offsety=151, wait_delta=1, times=1,success_image="log/logqueren.bmp",sim = 1.0)
            print("log success")
            return 1
    else:
        find_pic_loop(r"log/jinruyouxi.bmp", click_en=1, offsetx=399, offsety=151, wait_delta=1, times=5)
        find_pic_loop(r"log/jieshou.bmp", click_en=1, offsetx=399, offsety=151, wait_delta=1, times=5)
        find_pic_loop(r"log/dianjijinru.bmp", click_en=1, offsetx=399, offsety=151, wait_delta=1, times=1,success_image="log/logqueren.bmp|log/logqueren1.bmp",sim = 0.9)
        print("log success")
        return 1



#绑定逍遥窗口
hwnd = bind(2)

#account_list = open(r"D:\dm110\account.txt").read().split('\n')
#log(hwnd, account_list[0],account_list[1])
#log(hwnd)

dm.UnBindWindow()
