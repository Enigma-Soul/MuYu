from os import listdir
from os.path import basename
from os.path import isdir
from threading import Thread as Th
import pystray
from PIL import Image
from pystray import MenuItem as item
from time import sleep
from os import system
from pygame import init,mixer

import os
zid = False
# 数
file = ".\mod" #绝对路径
nem2 = 0


# 函数
def on_exit(icon, item):
    icon.stop()

def open_txt():
    system(file+r"\功德数.txt")
def icon(time):
    temp = listdir(mod_now+"/img")
    sl_time = round(time/(len(temp) * 2),5)
    for i in range(2):
        if i == 0:
            for x in range(int(len(temp))):
                img = Image.open(mod_now+"/img/"+"%s.ico" % str(int(x + 1)))
                tray_icon.icon = img

                sleep(sl_time)
        else:
            for x in range(int(len(temp))):
                img = Image.open(mod_now + "/img/" + "%s.ico" % str(int(len(temp) - x)))
                tray_icon.icon = img
                sleep(sl_time)
def add1():
    global nember
    with open(file + r"\功德数.txt","rb") as f:
        nember = int(f.readline())
        f.close()
    with open(file + r"\功德数.txt", "w") as f:
        f.write(str(nember+1))
        f.close()
    # 图标更换
    with open(mod_now+"/时间.txt") as f:
        time = float(f.readline())
        f.close()
    init()
    mixer.init()
    song = mixer.Sound(mod_now+"/MP3.mp3")
    song.play()
    Th(icon(time))
    mixer.stop()
def shuaxinn(icon, item):
    img = Image.open(mod_now + "/img/" + "1.ico")
    tray_icon.icon = img
def zidong(icon, item):
    global nem2
    while True:
        with open(file + "/自动数.txt") as f:
            nem1 = int(f.readline())
            f.close()
        if nem1 != nem2:
            nem2 = nem2 + 1
            with open(file + "/间隔时间.txt") as f:
                time = float(f.readline())
                f.close()
            sleep(time)
            add1()
        else:
            break

def Start():
    global mod_now
    mod_now = mod()[0]
    tray = create()
    tray.run()

def mod():
    list = []
    temp = listdir(file)
    for i in range(len(temp)):
        if isdir(file+"/"+temp[i]):
            list = list + [file+"/"+temp[i]]
    return list
def create():
    global tray_icon
    image = Image.open(mod_now + r"\img\1.ico")
    menu_items = []
    menu_items = menu_items + [item("   功德数TXT", open_txt), ]
    menu_items = menu_items + [pystray.Menu.SEPARATOR,]
    menu_items = menu_items + [item("    积攒功德", add1,default=True), ]
    menu_items = menu_items + [pystray.Menu.SEPARATOR, ]
    menu_items = menu_items + [item("  自动模式[开]", zidong), ]
    menu_items = menu_items + [pystray.Menu.SEPARATOR, ]
    menu_items = menu_items + [item("   更改材质包", None), ]
    for i in range(len(mod())):
        menu_items = menu_items + [item("%s" % basename(mod()[i]), change), ]
    menu_items = menu_items + [pystray.Menu.SEPARATOR, ]
    menu_items = menu_items + [item('    刷新木鱼', shuaxinn)]
    menu_items = menu_items + [item('    退出木鱼',on_exit)]
    tray_icon = pystray.Icon("name", image, "木鱼", menu_items)
    return tray_icon


def change(icon, item):
    global mod_now
    mod_now = file+"/"+str(item)
    img = Image.open(mod_now + "/img/" + "1.ico")
    tray_icon.icon = img
Th(Start())







