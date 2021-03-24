import os,sys
import subprocess
import pyautogui
import time
from gbf_functions import *
from python_imagesearch.imagesearch import imagesearch, imagesearch_count
#from os.path import expanduser
#home = expanduser("~")
#### hm
#summons = ["luci150.png"]

sk = 7
refresh = 2 * sk + 1
#char1 = {'pos': (x+110,y+640),'skills':[s1,s2]}
#char2 = {'pos': (x+200,y+640),'skills':[s1,s2]}
#char3 = {'pos': (x+290,y+640),'skills':[s3,s1]}
#char4 = {'pos': (x+380,y+640),'skills':[s1]}
#chars=[char1,char4]

#### ex
summons = ["bahu150.png"]
char1 = {'pos': (x+110,y+640),'skills':[s1,s2,s4]}
char2 = {'pos': (x+200,y+640),'skills':[s2]}
char3 = {'pos': (x+290,y+640),'skills':[s3]}
char4 = {'pos': (x+380,y+640),'skills':[s1,s2,s3]}
chars=[char1,char2,char3,char4]

#pos = imagesearch(home+image_dir+summons[0])
#print(home+image_dir+summons[0])

#sk how many seconds to wait after attack to hit F5



for i in range(4):
    sequence(refresh,chars,summons)
    i+=1
    print(i)
