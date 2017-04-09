# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from time import sleep
import mp3play
root = Tk()
f = mp3play.load('Biosaur - Dimensional Drift BGM.mp3')
play = lambda: f.play()
s = Canvas(root,width = 1200, height = 600)
s.pack()
musicTime = 0
######
#MAPS#
######
map1 = [
        [1,1,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,1],
        [0,0,0,0,0,1,1,1],
        ]
###########
#Variables#
###########
size = 3/4
player = 0
keys = [0,0,0,0,0,0,0,0]
x = 400
y = 400
w = 400
z = 400
speed = 2.5
game = True
blockx = []
blocky = []
blocks = []
newroom = True
currmap = map1
###########
#Functions#
###########
def collision(x,y,blockx,blocky):
    for i in range(len(blockx)):
        if x > blockx[i]-80*size:
            if x < blockx[i]+80*size:
                if y > blocky[i]-80*size:
                    if y < blocky[i]+80*size:
                        return True
            
def bindKey(key, bind):
    keys[key] = bind
import mp3play
#f = mp3play.load('Sound.mp3')
#play = lambda: f.play()

def roomgeneration(currmap,blockx,blocky):
    blockx = []
    blocky = []
    for i in range(len(currmap)):
        for u in range(len(currmap[i])):
            if currmap[i][u] == 1:
                blockx.append((u*100*size)+50*size)
                blocky.append((i*100*size)+50*size)
    return(blockx,blocky)


##############
#Key Bindings#
##############
root.bind("<Right>", lambda event: bindKey(0,1))
root.bind("<Left>", lambda event: bindKey(1,1))
root.bind("<Up>", lambda event: bindKey(2,1))
root.bind("<Down>", lambda event: bindKey(3,1))
root.bind("<KeyRelease-Right>", lambda event: bindKey(0,0))
root.bind("<KeyRelease-Left>", lambda event: bindKey(1,0))
root.bind("<KeyRelease-Up>", lambda event: bindKey(2,0))
root.bind("<KeyRelease-Down>", lambda event: bindKey(3,0))

root.bind("<d>", lambda event: bindKey(4,1))
root.bind("<a>", lambda event: bindKey(5,1))
root.bind("<w>", lambda event: bindKey(6,1))
root.bind("<s>", lambda event: bindKey(7,1))
root.bind("<KeyRelease-d>", lambda event: bindKey(4,0))
root.bind("<KeyRelease-a>", lambda event: bindKey(5,0))
root.bind("<KeyRelease-w>", lambda event: bindKey(6,0))
root.bind("<KeyRelease-s>", lambda event: bindKey(7,0))
###########
#Main Loop#
###########
while game == True:
    if keys[0] == 1:
        if collision(x+speed,y,blockx,blocky) != True:
            x += speed
    if keys[1] == 1:
        if collision(x-speed,y,blockx,blocky) != True:
            x -= speed
    if keys[2] == 1:
        if collision(x,y-speed,blockx,blocky) != True:
            y -= speed
    if keys[3] == 1:
        if collision(x,y+speed,blockx,blocky) != True:
            y += speed
    if newroom == True:
        newroom = False
        blockx,blocky = roomgeneration(currmap,blockx,blocky)
    
    if musicTime == 0:
        play()
    musicTime ++
    if musicTime == 1600
        musicTime = 0

    ##############
    #Frame Update#
    ##############
    s.delete("all")
    for i in range(len(blockx)):
        s.create_rectangle(blockx[i]+50*size,blocky[i]+50*size,blockx[i]-50*size,blocky[i]-50*size,fill="black")
    player = s.create_rectangle(x+30*size,y+30*size,x-30*size,y-30*size,fill="blue")
    s.update()
    sleep(0.01)