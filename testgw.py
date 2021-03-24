
import pyautogui, sys

import time
import win32gui
import win32con
import win32api
from python_imagesearch.imagesearch import imagesearch, imagesearch_count

h = win32gui.FindWindow("Chrome_WidgetWin_1", "Granblue Fantasy - Google Chrome")
#print(h)
win32gui.SetForegroundWindow(h)
xtop,ytop,xbot,ybot = win32gui.GetWindowRect(h)


def claim():
    pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\ok_exp.png")
    pyautogui.moveTo(xtop+270,ytop+740)
    time.sleep(.5)
    #click for EMP
    pyautogui.doubleClick()
    while pos[0] != -1:
        time.sleep(1)
        pyautogui.moveTo(xtop+270,ytop+540)
        time.sleep(.5)
        #click for EMP
        pyautogui.doubleClick()
        pyautogui.moveTo(pos[0]+10,pos[1]+10)
        pyautogui.click()
        pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\ok_exp.png")



def play_again():
    pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\play_again.png")
    pyautogui.moveTo(pos[0]+50,pos[1]+30)

play_again()