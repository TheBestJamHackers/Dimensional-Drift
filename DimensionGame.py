# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from time import sleep
root = Tk()
s = Canvas(root,width = 800, height = 800)
s.pack()
###########
#Variables#
###########
player = 0
keys = [0,0,0,0,0,0,0,0]
x = 400
y = 400
w = 400
z = 400
size = 20
speed = 3
game = True
###########
#Functions#
###########
def bindKey(key, bind):
    keys[key] = bind

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
        x += speed
    if keys[1] == 1:
        x -= speed
    if keys[2] == 1:
        y -= speed
    if keys[3] == 1:
        y += speed
    ##############
    #Frame Update#
    ##############
    s.delete(player)
    player = s.create_rectangle(x-size,y-size,x+size,y+size,fill="blue")
    s.update()
    sleep(0.01)