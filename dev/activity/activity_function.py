from util.dm import *

def activity_power_get():
    ret = find_pic_loop('activity/power_get.bmp',success_image='activity/power_get_success.bmp',times= 200)
    if(ret == ""):
        return 0
    return 1

if __name__ == '__main__':
    activity_power_get()