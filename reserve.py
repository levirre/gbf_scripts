#reserve.py

import pyautogui, sys

import time
import win32gui
import win32con
import win32api
from python_imagesearch.imagesearch import imagesearch, imagesearch_count, imagesearcharea

h = win32gui.FindWindow("Chrome_WidgetWin_1", "Granblue Fantasy - Google Chrome")
#print(h)
win32gui.SetForegroundWindow(h)
xtop,ytop,xbot,ybot = win32gui.GetWindowRect(h)

def reserve():
    time.sleep(.8)
    #pos = imagesearcharea(f"C:\\Users\\loli\\Desktop\\gbf macro\\reserve.png",700,530,1268,954)
    #print(pos[0],pos[1])
    pyautogui.moveTo(1050,600)
    pyautogui.click()

def ok():
    for i in range(3):
        time.sleep(.8)
        pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\ok_c.png")
        pyautogui.moveTo(pos[0]+20,pos[1]+20)
        pyautogui.click()



for i in range(300):
    reserve()
    ok()

#reserve()