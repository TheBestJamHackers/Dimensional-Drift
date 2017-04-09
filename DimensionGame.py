from tkinter import *
from time import sleep
root = Tk()
s = Canvas(root,width = 1200, height = 600)
s.pack()
######
#MAPS#
######
map1 = [[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]
        ],[
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
        ],[
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]
        ],[
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ],
        [[1,1,1,1],
         [1,0,0,1],
         [1,0,0,1],
         [1,1,1,1]
         ],
        [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]
        ]
map2 = []
map3 = []
map4 = []
map5 = []
###########
#Variables#
###########
size = 3/4
player = 0
keys = [0,0,0,0,0,0,0,0]
x = 0
y = 0
w = 0
z = 0
game = True
blockx = []
blocky = []
blocks = []
currmap = map1
level = 0
levelupdate = True

########
#Images#
########
imgblock = PhotoImage (file = "Images/Environment/Block.ppm")
imgplayer = PhotoImage (file = "Images/Robot/bot front.ppm")

###########
#Functions#
###########
def levelup(level):
    if level==1:
        return(map1)
    elif level==2:
        return(map2)
    elif level==3:
        return(map3)
    elif level==4:
        return(map4)
    elif level==5:
        return(map5)

def bindKey(key, bind):
    keys[key] = bind

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
    if levelupdate == True:
        x = 0
        y = 0
        w = 0
        z = 0
        levelupdate = False
        level+=1
        currmap = levelup(level)
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
    for x2 in range(len(currmap)):
        for y2 in range(len(currmap[x2])):
            if currmap[x2][y2][z][w] == 1:
                s.create_image(
                        x2 * 100 * size + 150 * size,
                        y2 * 100 * size + 150 * size,
                        image=imgblock)
    
    for z2 in range(len(currmap[x][y])):
        for w2 in range(len(currmap[x][y][z2])):
            if currmap[x][y][z2][w2] == 1:
                s.create_image(
                    z2 * 100 * size + 750 * size, 
                    w2 * 100 * size + 150 * size,
                    image=imgblock)

    player = s.create_image(x*100*size+150*size,y*100*size+150*size,image=imgplayer)
    plawer = s.create_image(z*100*size+750*size,w*100*size+150*size,image=imgplayer)
    s.update()
    sleep(0.1)
