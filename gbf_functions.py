#gbf_functions.py
import os,sys
import subprocess
import pyautogui
import time
#import gbf_functions
from python_imagesearch.imagesearch import imagesearch, imagesearch_count
from os.path import expanduser

win_pos = subprocess.getoutput("wmctrl -lG | grep Granblue | awk '{print $3,$4}'")
x,y=list(map(int, win_pos.split(' ')))
CENTER =20
home = expanduser("~")
image_dir = "/gbf_macro/"
os.system("wmctrl -a Granblue")

summon=(x+450,y+650)
support=(x+500,y+650)
#pyautogui.moveTo(skill4[0],skill4[1])
s1=(x+220,y+650)
s2=(x+310,y+650)
s3=(x+390,y+650)
s4=(x+470,y+650)

def back():
    pyautogui.moveTo(x+120,y+490)
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
    #pyautogui.moveTo(x+120,y+500)
    pyautogui.moveTo(x+410,y+610)
    time.sleep(1)
    pyautogui.click()
    back()
def clickattack():
    pyautogui.moveTo(x+430,y+500)
    time.sleep(1)
    pyautogui.click()
def refresh(t: int):
    time.sleep(t)
    pyautogui.press('f5',presses=1) 

def search_summons(summons: list):
    summons= summons

    for i in range(len(summons)):
        print(home+image_dir+summons[i])
        pos = imagesearch(home+image_dir+summons[i])
        if pos[0] != -1:
                pyautogui.moveTo(pos[0],pos[1])
                time.sleep(1)
                pyautogui.click()
                #click ok
                time.sleep(1)
                pyautogui.moveTo(x+420,y+760)
                time.sleep(1)
                pyautogui.click()
                break
                
        else:
            pyautogui.press('down',presses=10) 
            time.sleep(2)
            pos = imagesearch(summons[i])
            if pos[0] != -1:
                time.sleep(1)
                pyautogui.moveTo(pos[0],pos[1])
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x+420,y+760)
                time.sleep(1)
                pyautogui.click()
                break

def claim():
    pyautogui.moveTo(x+300,y+600)
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x+300,y+760)
    time.sleep(2)
    pyautogui.click()

def play_again():
    pyautogui.moveTo(x+190,y+530)
    time.sleep(1)
    pyautogui.click()
#time.sleep(3)

def sequence(t: int,chars: list,summons: list):
    search_summons(summons)
    time.sleep(9)
    clicksummon()
    time.sleep(3)
    clickchars(chars)
    clickattack()
    refresh(t)
    time.sleep(6)
    claim()
    time.sleep(1.5)
    play_again()
    time.sleep(3)
