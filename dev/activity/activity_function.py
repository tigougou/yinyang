from util.dm import *

def activity_power_get():
    ret = find_pic_loop('activity/power_get.bmp',times= 100)
    if(ret == ""):
        return 0
    time.sleep(10)
    moveto(45,163)
    left_click()
    return 1
if __name__ == '__main__':
    ret = find_pic_loop('activity/power_get_success.bmp',offsetx=79,offsety=158,times= 20)