from util.dm import *

def activity_power_get():
    ret = find_pic_loop('activity/power_get.bmp',times= 100)
    if(ret == ""):
        return 0
    ret = find_pic_loop('activity/power_get_success.bmp',offsetx=79,offsety=158,times= 20)
    if ret == "":
        return 0
    else:
        for i in range(10):
            ret = find_pic_loop('activity/power_get_success.bmp',offsetx=79,offsety=158,times= 20)
            if ret == "":
                return 1

    return 1

if __name__ == '__main__':
    activity_power_get()