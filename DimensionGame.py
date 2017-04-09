# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from time import sleep
root = Tk()
s = Canvas(root,width = 1200, height = 600)
s.pack()
######
#MAPS#
######
map1 = [[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ],[
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ],[
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ],[
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ]
###########
#Variables#
###########
size = 3/4
player = 0
keys = [0,0,0,0,0,0,0,0]
x = 2
y = 2
w = 2
z = 2
game = True
blockx = []
blocky = []
blocks = []
currmap = map1

########
#Images#
########
imgblock = PhotoImage (file = "Images/Environment/Block.pgm")

###########
#Functions#
###########
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
root.bind("<Right>", lambda event: bindKey(4,1))
root.bind("<Left>", lambda event: bindKey(5,1))
root.bind("<Up>", lambda event: bindKey(6,1))
root.bind("<Down>", lambda event: bindKey(7,1))

root.bind("<d>", lambda event: bindKey(0,1))
root.bind("<a>", lambda event: bindKey(1,1))
root.bind("<w>", lambda event: bindKey(2,1))
root.bind("<s>", lambda event: bindKey(3,1))
###########
#Main Loop#
###########
while game == True:
    if keys[0] == 1:
        if x+1<4:
            if currmap[x+1][y][z][w] != 1:
                x += 1
    if keys[1] == 1:
        if x-1>-1:
            if currmap[x-1][y][z][w] != 1:
                x -= 1
    if keys[2] == 1:
        if y-1>-1:
            if currmap[x][y-1][z][w] != 1:            
                y -= 1
    if keys[3] == 1:
        if y+1<4:
            if currmap[x][y+1][z][w] != 1:
                y += 1
    if keys[4] == 1:
        if z+1<4:
            if currmap[x][y][z+1][w] != 1:
                z += 1
    if keys[5] == 1:
        if z-1>-1:
            if currmap[x][y][z-1][w] != 1:
                z -= 1
    if keys[6] == 1:
        if w-1>-1:
            if currmap[x][y][z][w-1] != 1:            
                w -= 1
    if keys[7] == 1:
        if w+1<4:
            if currmap[x][y][z][w+1] != 1:
                w += 1
    keys = [0,0,0,0,0,0,0,0]


    ##############
    #Frame Update#
    ##############
    s.delete("all")
    for i in range(len(blockx)):
        s.create_image(blockx[i]+50*size,blocky[i]+50*size,blockx[i]-50*size,blocky[i]-50*size, image=imgblock)
    player = s.create_rectangle(x*100+150*size,y*100+150*size,x*100+50*size,y*100+50*size,fill="blue")
    plawer = s.create_rectangle(z*100+750*size,w*100+150*size,z*100+650*size,w*100+50*size,fill="blue")
    s.update()
    sleep(0.1)