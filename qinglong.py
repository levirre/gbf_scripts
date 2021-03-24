#zhuque.py
#qinglong.py

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

def findclick(pos):
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(x=pos[0]+10, y= pos[1]+10)
        time.sleep(2)
    else:
        print("image not found")
##I want chardata= portrait to click, skills to click
#char1=(xtop+110,ytop+650)
#char2=(xtop+200,ytop+650)
#char3=(xtop+280,ytop+650)
#char4=(xtop+360,ytop+650)
summon=(xtop+450,ytop+650)
support=(xtop+500,ytop+650)
#pyautogui.moveTo(skill4[0],skill4[1])
s1=(xtop+220,ytop+650)
s2=(xtop+310,ytop+650)
s3=(xtop+390,ytop+650)
s4=(xtop+470,ytop+650)
def back():
    pyautogui.moveTo(xtop+120,ytop+490)
    time.sleep(1)
    pyautogui.click()

def clickchars(chars: list):
    for i in chars:
        pyautogui.moveTo(i['pos'][0],i['pos'][1])
        time.sleep(1)
        pyautogui.click()
        clickskills(i['skills'])
        back()
    

def clickskills(skills: list):
    for i in skills:
        pyautogui.moveTo(i[0],i[1])
        time.sleep(.5)
        pyautogui.click(clicks=2)
def clicksummon():
    pyautogui.moveTo(summon[0],summon[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(support[0],support[1])
    time.sleep(1)
    pyautogui.click()
    #pyautogui.moveTo(xtop+120,ytop+500)
    pyautogui.moveTo(xtop+410,ytop+610)
    time.sleep(1)
    pyautogui.click()
    back()
def clickattack():
    pyautogui.moveTo(xtop+430,ytop+500)
    time.sleep(1)
    pyautogui.click()
def refresh(t: int):
    time.sleep(t)
    pyautogui.press('f5',presses=1) 

def findclick(pos):
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        time.sleep(1)
        pyautogui.click(x=pos[0] +20, y= pos[1])
        time.sleep(1)
    else:
        print("image not found")

#char1=(xtop+110,ytop+650)
#char2=(xtop+200,ytop+650)
#char3=(xtop+280,ytop+650)
#char4=(xtop+360,ytop+650)

def claim():
    pyautogui.moveTo(xtop+300,ytop+590)
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(xtop+300,ytop+740)
    time.sleep(2)
    pyautogui.click()

#time.sleep(3)

def play_again():
    pyautogui.moveTo(xtop+190,ytop+530)
    time.sleep(1)
    pyautogui.click()

def search_summons():
    summons= ["shiva140.png","colo140.png"]
    for i in range(0,len(summons)):
        pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{summons[i]}")
        if pos[0] != -1:
                findclick(pos)
                pyautogui.moveTo(xtop+420,ytop+760)
                time.sleep(1)
                pyautogui.click()
                break
                
        else:
            pyautogui.press('down',presses=10) 
            time.sleep(2)
            pos = imagesearch(f"C:\\Users\\loli\\Desktop\\gbf macro\\{summons[i]}")
            if pos[0] != -1:
                findclick(pos)
                pyautogui.moveTo(xtop+420,ytop+760)
                time.sleep(1)
                pyautogui.click()
                break


char1 = {'pos': (xtop+110,ytop+640),'skills':[s4,s2,s3,s1]}
char2 = {'pos': (xtop+200,ytop+640),'skills':[s1]}
char3 = {'pos': (xtop+290,ytop+640),'skills':[s2,s1]}
char4 = {'pos': (xtop+380,ytop+640),'skills':[s2]}
chars=[char4,char1,char2,char3]


def sequence():
    
    search_summons()
    time.sleep(9)
    #pyautogui.moveTo(xtop+220,ytop+360)
    #time.sleep(1)
    #pyautogui.click(clicks=2)
    time.sleep(1)
    clicksummon()
    time.sleep(3)
    clickchars(chars)
    clickattack()
    refresh(8)
    time.sleep(3)
    claim()
    time.sleep(2)
    play_again()
    time.sleep(2)

for i in range(8):
    sequence()
    i+=1
    print(i)


