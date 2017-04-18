import os
from tkinter import *
from time import sleep
if os.name=="nt":
    import winsound
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
root = Tk()
s = Canvas(root,width = 900, height = 450)
s.pack()
######
#MAPS#
######
map1 = [[[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[2,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]]
        ],[
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],

        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ]

map2 = [[[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]]
        ],[
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[2,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ]
map3 = [[[0,0,1,2],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[1,0,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]]
        ],[
        [[1,0,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,1,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,0,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,0,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ],[
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,0,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ],
        [[1,0,0,0],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]
         ]
        ]
map4 = [[[0,1,0,0],
         [1,1,0,0],
         [1,1,0,0],
         [0,0,0,0]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ]
        ],[
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]]
        ],[
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,0,1,1]
         ],
        [[0,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,0,1,1]
         ],
        [[0,0,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,0,1,1]
         ],
        [[1,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,0,1,1]
         ]
        ],[
        [[1,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[1,1,0,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,1]
         ],
        [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [2,0,1,1]
         ]
        ]

map5 = []

###########
#Variables#
###########
size = 3/4
player = 0
keys = [0,0,0,0,0,0,0,0,0,0,0]
x = 2
y = 2
w = 2
z = 2
game = True
blockx = []
blocky = []
blocks = []
currmap = map1
musicTime = 0
levelUpdate = True
level = 0
gamemode = 0
save = ""

########
#Images#
########
imgblock = PhotoImage (file = "Images/Environment/Block.ppm")
imgplayer = PhotoImage (file = "Images/Robot/bot front.ppm")
imgplawer = PhotoImage (file = "Images/Robot/bot front.ppm")
imggrid = PhotoImage (file = "Images/Environment/Grid.ppm")
imgbg = PhotoImage (file = "Images/Environment/Background.ppm")

###########
#Functions#
###########
def bindKey(key, bind):
    keys[key] = bind

def levelup(level):
    if level == 1:
        return map1
    if level == 2:
        return map2
    if level == 3:
        return map3
    if level == 4:
        return map4
    if level == 5:
        return map1

##############
#Key Bindings#
##############
root.bind("<Right>", lambda event: bindKey(4,1))
root.bind("<Left>", lambda event: bindKey(5,1))
root.bind("<Up>", lambda event: bindKey(6,1))
root.bind("<Down>", lambda event: bindKey(7,1))

root.bind("d", lambda event: bindKey(0,1))
root.bind("a", lambda event: bindKey(1,1))
root.bind("w", lambda event: bindKey(2,1))
root.bind("s", lambda event: bindKey(3,1))
root.bind("1", lambda event: bindKey(8,1))
root.bind("2", lambda event: bindKey(9,1))
root.bind("3", lambda event: bindKey(10,1))

root.bind("4", lambda event: bindKey(11,1))

###########
#Main Loop#
###########

while game == True:

    
    if currmap[x][y][z][w] == 2:
        levelUpdate = True

    if musicTime == 0:
        if os.name=="nt":
            winsound.PlaySound('BGM.wav', winsound.SND_ASYNC)
    musicTime += 1
    if musicTime == 160:
        musicTime = 0

    if levelUpdate == True:
        x = 0
        y = 0
        w = 0
        z = 0
        levelUpdate = False
        level+=1
        currmap = levelup(level)
        
    if keys[8] == 1:
        if gamemode != 1:
            gamemode = 1
        else:
            gamemode = 0
            
    if keys[0] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot right.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot right.ppm")
        if x+1<4:
            if gamemode != 1:
                if currmap[x+1][y][z][w] != 1:
                    x += 1
            else:
                x += 1
    if keys[1] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot left.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot left.ppm")
        if x-1>-1:
            if gamemode != 1:
                if currmap[x-1][y][z][w] != 1:
                    x -= 1
            else:
                x -= 1
    if keys[2] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot up.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot front.ppm")
        if y-1>-1:
            if gamemode != 1:
                if currmap[x][y-1][z][w] != 1:            
                    y -= 1
            else:
                y -= 1
    if keys[3] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot down.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot back.ppm")
        if y+1<4:
            if gamemode != 1:
                if currmap[x][y+1][z][w] != 1:
                    y += 1
            else:
                y += 1
    if keys[4] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot right.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot right.ppm")
        if z+1<4:
            if gamemode != 1:
                if currmap[x][y][z+1][w] != 1:
                    z += 1
            else:
                z += 1
    if keys[5] == 1:
        imgplawer = PhotoImage (file = "Images/Robot/bot left.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot left.ppm")
        if z-1>-1:
            if gamemode != 1:
                if currmap[x][y][z-1][w] != 1:
                    z -= 1
            else:
                z -= 1
    if keys[6] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot front.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot up.ppm")
        if w-1>-1:
            if gamemode != 1:
                if currmap[x][y][z][w-1] != 1:            
                    w -= 1
            else:
                w -= 1
    if keys[7] == 1:
        imgplayer = PhotoImage (file = "Images/Robot/bot back.ppm")
        imgplawer = PhotoImage (file = "Images/Robot/bot down.ppm")
        if w+1<4:
            if gamemode != 1:
                if currmap[x][y][z][w+1] != 1:
                    w += 1
            else:
                w += 1
                
    if keys[11] == 1:
        a = ""
        save = ""
        for p in range(4):
            for q in range(4):
                for r in range(4):
                    for s in range(4):
                        a += str(currmap[p][q][r][s])
                    save += chr(int(a,3))
                    a = ""
        open("levels.txt","w").write(save)
        
                
    keys = [0,0,0,0,0,0,0,0,0,0,0]


    ##############
    #Frame Update#
    ##############
    s.delete("all")

    s.create_image(450, 225, image=imgbg)
    s.create_image(300*size, 300*size, image=imggrid)
    s.create_image(900*size, 300*size, image=imggrid)

    for x2 in range(len(currmap)):
        for y2 in range(len(currmap[x2])):
            if currmap[x2][y2][z][w] == 1:
                s.create_image(
                        x2 * 100 * size + 150 * size,
                        y2 * 100 * size + 150 * size,
                        image=imgblock)
            if currmap[x2][y2][z][w] == 2:
                s.create_oval(
                        x2 * 100 * size + 100 * size,
                        y2 * 100 * size + 100 * size,
                        x2 * 100 * size + 200 * size,
                        y2 * 100 * size + 200 * size,fill="yellow")
    
    for z2 in range(len(currmap[x][y])):
        for w2 in range(len(currmap[x][y][z2])):
            if currmap[x][y][z2][w2] == 1:
                s.create_image(
                    z2 * 100 * size + 750 * size, 
                    w2 * 100 * size + 150 * size,
                    image=imgblock)
            if currmap[x][y][z2][w2] == 2:
                s.create_oval(
                    z2 * 100 * size + 700 * size, 
                    w2 * 100 * size + 100 * size,
                    z2 * 100 * size + 800 * size, 
                    w2 * 100 * size + 200 * size,fill="yellow")

    player = s.create_image(x*100*size+150*size,y*100*size+150*size,image=imgplayer)
    plawer = s.create_image(z*100*size+750*size,w*100*size+150*size,image=imgplawer)
    
    s.update()
    sleep(0.1)
