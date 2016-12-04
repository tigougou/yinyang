import win32com.client
import time
regInfoFile = open(r"D:\dm110\regInfo.txt")
dm = win32com.client.Dispatch('dm.dmsoft')
print(dm.Ver())
regInfoList = regInfoFile.read().split('\n')
dm.SetPath("D:\dm110")
dm_ret = dm.Reg(regInfoList[0],regInfoList[1])
hwnd = dm.FindWindow('BS2CHINAUI','Bluestacks App Player')
print("find bluestack! hwnd: " + str(hwnd))
hwnd = dm.EnumWindow(hwnd,"","",0)
#print("hwnd: " + str(hwnd))
hwnds = hwnd.split(',')
for id in hwnds:
    print(str(id) + ": " + dm.GetWindowClass(id) + " titile: " + dm.GetWindowTitle(id))
    if(dm.GetWindowClass(id) == "WindowsForms10.Window.8.app.0.34f5582_r14_ad1" and dm.GetWindowTitle(id) == ""):
        ret = dm.BindWindowEx(id, "gdi", "dx", "dx", "dx", 0)
        print(ret)
dm.MoveTo(486,576)
dm.LeftClick()
dm.UnBindWindow()
