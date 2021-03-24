import pyautogui, sys

import time
#x,y,w,h=pyautogui.locateOnScreen('C:\\Users\\loli\\Desktop\\gbf macro\\test.png')

#pyautogui.click(x=x+50, y=y+50)
#time.sleep(5)
#x,y,w,h=pyautogui.locateOnScreen('C:\\Users\\loli\\Desktop\\gbf macro\\ok.png')
#pyautogui.click(x=x+50, y=y+50)

import win32gui
import win32con
import win32api
from python_imagesearch.imagesearch import imagesearch, imagesearch_count

h = win32gui.FindWindow("Chrome_WidgetWin_1", "Granblue Fantasy - Google Chrome")
#print(h)
win32gui.SetForegroundWindow(h)
xtop,ytop,xbot,ybot = win32gui.GetWindowRect(h)
#print(f"{x} {y}")
def findclick(pos):
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(x=pos[0] +20, y= pos[1] + 20)
        time.sleep(2)
    else:
        print("image not found")
summons= ["yss 140.png","alex.png"]
seq = ["summon.png","uru.png","ok summon.png","vohu.png","ok summon.png","cag.png","1.png","2.png","arrow.png","3.png","4.png","5.png","6.png","arrow.png","7.png","arrow.png","8.png","9.png","attack.png"]
for x in range(0,20):



    pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\play_again.png")
    findclick(pos)
#pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{summons[0]}")
#findclick(pos)
#pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\play_again.png")
#findclick(pos)

#for x in range( 0,30):
    pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{summons[0]}",.9)
#print(str(pos))
    if pos[0] == -1:
        pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{summons[1]}",.9)
    findclick(pos)
    pos = imagesearch("C:\\Users\\loli\\Desktop\\gbf macro\\ok.png")
    findclick(pos)
    time.sleep(6)
#pos = imagesearch("C:\\Users\\loli\\Desktop\\gbf macro\\ok.png")

    

    for s in seq:
        pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{s}")
        findclick(pos)
        time.sleep(2)
    pyautogui.press('f5')
    time.sleep(4)
    pos = imagesearch("C:\\Users\\loli\\Desktop\\gbf macro\\attack.png")
    while pos[0] != -1:
        findclick(pos)
        time.sleep(4)

    time.sleep(4)
    pos = imagesearch("C:\\Users\\loli\\Desktop\\gbf macro\\ok.png",0.7)
    ok_clicks = 0
    while ok_clicks < 2:
        if pos[0] == -1:
            pyautogui.click()
            time.sleep(1)
            print(ok_clicks)
            pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\ok.png",0.7)
        else:
            pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\ok.png",0.7)
            findclick(pos)
            ok_clicks = ok_clicks +1
        
        
    
    pos = imagesearch("C:\\Users\\loli\\Desktop\\gbf macro\\play_again.png",0.7)
    findclick(pos)

#if pos[0] != -1:
#    print("position : ", pos[0], pos[1])
#    pyautogui.click(x=pos[0] +20, y= pos[1] + 20)
#else:
#    print("image not found")