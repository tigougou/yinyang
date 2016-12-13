import win32com.client
import time
regInfoFile = open(r"D:\dm110\regInfo.txt")
dm = win32com.client.Dispatch('dm.dmsoft')
print(dm.Ver())
regInfoList = regInfoFile.read().split('\n')
dm.SetPath("D:\dm110")
dm.SetDict(0,"process\dm_soft.txt")
dm.UseDict(0)
dm_ret = dm.Reg(regInfoList[0],regInfoList[1])
"""
绑定模拟器函数
Parameters:
  type - 模拟器类型 1：blustacks 2：逍遥安卓
Returns:
  成功：返回 1
  失败：返回 0
Raises:
"""
def WindowBind(type):
    if(type == 1):
        hwnd = dm.FindWindow('BS2CHINAUI','Bluestacks App Player')
        print("find bluestack! hwnd: " + str(hwnd))
        hwnd = dm.EnumWindow(hwnd, "", "", 0)
        hwnds = hwnd.split(',')
        for id in hwnds:
            #print(str(id) + ": " + dm.GetWindowClass(id) + " titile: " + dm.GetWindowTitle(id))
            if (dm.GetWindowClass(id).startswith("WindowsForms10.Window.8.app.") and dm.GetWindowTitle(id) == ""):
                print("binding hwnd: " + str(id))
                ret = dm.BindWindowEx(id, "dx2", "dx", "dx","dx", 0)
                if(ret != 0):
                    print("bind success!")
                    return id
                else:
                    print("bind failed")
                    return 0

        print("bind failed")
    elif(type == 2):
        hwnd = dm.FindWindow('Qt5QWindowIcon','逍遥安卓 2.9.1 - MEmu')
        hwnd = dm.EnumWindow(hwnd,"Qt5QWindowIcon","RenderWindowWindow",0)
        print("find xiaoyao! hwnd: " + str(hwnd))
        hwnds = hwnd.split(',')
        for id in hwnds:
            #print(str(id) + ": " + dm.GetWindowClass(id) + " titile: " + dm.GetWindowTitle(id))
            if (dm.GetWindowClass(id) == "Qt5QWindowIcon" and dm.GetWindowTitle(id) == "RenderWindowWindow"):
                ret = dm.BindWindowEx(id, "dx.graphic.opengl", "dx", "dx", "dx", 0)
                if (ret != 0):
                    print("bind success!")
                    return id
                else:
                    print("bind failed")
                    return 0
    else:
        return 0

"""
找图接口函数
Parameters:
  image - 图片名称
  x1,y1,x2,y2  - 找图坐标
  offsetx,offsety - 点击偏移点
  mode - 查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
  delta_color -偏色
  sim - 相似度
Returns:
  成功：返回 "id,x,y|id,x,y..|id,x,y"
  失败：返回 ""
Raises:
"""
def find_pic(image,delta_color = "000000",offsetx = 0,offsety = 0,mode = 0,x1 = 0, y1 = 0, x2 = 1280, y2 = 720, sim = 0.8):
    image_pos_find = dm.FindPicEx(x1, y1, x2, y2, image, delta_color, sim, mode)
    print("finding image: " + image)
    if(not image_pos_find):
        return ""
    print('find pic: ' + image_pos_find)
    return image_pos_find
"""
循环找图点击接口函数
Parameters:
  image - 图片名称
  x1,y1,x2,y2  - 找图坐标
  offsetx,offsety - 点击偏移点
  mode - 查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
  delta_color -偏色
  sim - 相似度
  click_en - 是否点击 1：点击 其他：不点击
  times - 循环次数
  wait_delta - 等待间隔时间（秒为单位）
  success_image - 点击成功判断标志
Returns:
  成功：返回 "id,x,y|id,x,y..|id,x,y"
  失败：返回 ""
Raises:
"""

def find_pic_loop(image,delta_color = "000000",click_en = 1,offsetx = 0,offsety = 0,mode = 0,x1 = 0, y1 = 0, x2 = 1280, y2 = 720, sim = 0.8,times = 10, wait_delta = 0.1, success_image = "",click_wait = 1):

    for i in range(times):
        image_pos_find = find_pic(image,delta_color = delta_color,offsetx = offsetx,offsety = offsety,mode = mode,x1 = x1, y1 = y1, x2 = x2, y2 = y2, sim = sim)
        if(image_pos_find != ""):
            if (click_en == 1):

                print('click pic: ' + image)
                find = image_pos_find.split('|')
                find = find[0].split(',')
                x = int(find[1])
                y = int(find[2])
                dm.Moveto(x + offsetx, y + offsety)
                dm.LeftClick()
            if (success_image != ""):
                while (True):
                    print("finding success_image: " + success_image)
                    find = find_pic(success_image, delta_color=delta_color, offsetx=offsetx, offsety=offsety, mode=mode,
                                    x1=x1, y1=y1, x2=x2, y2=y2, sim=sim)
                    if (find == ""):
                        find = find_pic(image, delta_color=delta_color, mode=mode, x1=x1, y1=y1, x2=x2, y2=y2, sim=sim)
                        if (find != ""):
                            find = find.split('|')
                            find = find[0].split(',')
                            x = int(find[1])
                            y = int(find[2])
                            dm.Moveto(x + offsetx, y + offsety)
                            dm.LeftClick()
                            print("left click!")
                            time.sleep(1)
                        else:
                            continue
                    else:
                        break

            return image_pos_find
        else:
            time.sleep(wait_delta)
    return ""

"""
根据找图结果得到第n个位置函数
Parameters:
  n - 第n个坐标
Returns:
  成功：返回 x，y
  失败：返回 ""
Raises:
"""
def get_pos(find_pos, n):
    positons = find_pos.split('|')
    for positon in positons:
        elements = positon.split(',')
        if(elements[0] == str(n)):
            return int(elements[1]),int(elements[2])
    return ""
"""
键鼠操作系列函数
Parameters:

Returns:
  成功：1
  失败：0
Raises:
"""
def moveto(x,y):
    return dm.Moveto(x,y)
def left_click():
    return dm.LeftClick()
def left_double_click():
    return dm.LeftDoubleClick
def left_down():
    return dm.LeftDown()
def left_up():
    return dm.LeftUp()
def whelldown():
    return dm.WheelDown()
def whellup():
    return dm.Wheelup()
def key_press_str(str,delay):
    return dm.KeyPressStr(str,delay)
def send_string(hwnd, str):
    return dm.SendString(hwnd, str)
def get_str(x1, y1, x2, y2, color = "000000-000000", sim = 0.9):
    return dm.Ocr(x1, y1, x2, y2, color, sim)
def unbind_window():
    return dm.UnBindWindow()



