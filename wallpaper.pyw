import random
import requests
import os
import time
import ctypes
from PIL import Image

width = 1920
height = 1080
w = 16
h = 9

def get_url():
    index = random.randint(0, 2612)
    file = open("addresses.txt")
    for i, line in enumerate(file):
        if i == index:
            url = 'https://www.gstatic.com/prettyearth/assets/full/' + line[:-1] + '.jpg'
            break
    return url
    file.close()

def get_wallpaper(width, height, w, h, c):
    f = open('temp.jpg', 'wb')
    img = requests.get(get_url())
    f.write(img.content)
    f.close()
    img = Image.open('temp.jpg')
    img = img.crop((0, 0, w*c, h*c))
    img = img.resize((width, height))
    img.save('temp1.jpg')
    os.remove('temp.jpg')

def set_wallpaper(width, height, w, h):
    path = os.getcwd()+'\\temp1.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
    a = 1800 // w
    b = 1200 // h

    if a < b:
        c = a
    else:
        c = b
        
    get_wallpaper(width, height, w, h, c)

set_wallpaper(width, height, w, h)
