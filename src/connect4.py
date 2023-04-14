from random import randint
from os import system

def clear(text):
     system("cls")
     print("Game Catalog > " + text)

def win(c4b, x, y, turn):
    adj = [[-3,-2,-1,0],[-2,-1,0,1],[-1,0,1,2],[0,1,2,3],[3,2,1,0],[2,1,0,-1],[1,0,-1,-2],[0,1,2,3],[0,0,0,0]]
    winx = [0,1,2,3,8,8,8,8]
    winy = [8,8,8,8,0,1,2,3]
    
    for i in range(len(winx)):
        ox = adj[winx[i]]
        oy = adj[winy[i]]

        ts = []
        for j in range(4):
             tx = x + ox[j]
             ty = y + oy[j]
             if not (tx < 0 or tx > 6 or ty < 0 or ty > 5):
                  ts.append(c4b[tx][ty])

        if len(ts) == 4:
             if turn == ts[0] == ts[1] == ts[2] == ts[3]:
                  return turn

    #detect if all board squares are filled, if nobody won it's a draw
    if not 0 in (c4b[0]+c4b[1]+c4b[2]+c4b[3]+c4b[4]+c4b[5]+c4b[6]):
         return 3
    
    #nobody won
    return 0

def showboard(c4b):
     markers = [".", "@", "O"]
     for i in range(6):
          line = [c4b[x][5-i] for x in range(7)]
          text = [markers[x] for x in line]
          print("   ".join(text))
          print("")

def connect4():
    c4b = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],]
    heights = [0,0,0,0,0,0,0]

    while True:
        clear("Connect 4")
        showboard(c4b)

        #player move
        pin = -1
        while True:
            pin = input("Pick an available collumn from 1-7: ")
            if pin.isnumeric():
                pin = int(pin) - 1
                if pin >= 0 and pin <= 6:
                    if sum([x!=0 for x in c4b[pin]]) < 6:
                        break
        
        c4b[pin][heights[pin]] = 1
        w = win(c4b, heights[pin], pin, 1)
        showboard(c4b)
        if w == 1:
            print("You won!")
            break
        elif w == 3:
            print("It's a draw.")
            break
        heights[pin] += 1

        #computer move
        while True:
            cin = randint(0, 6)
            if sum([x!=0 for x in c4b[cin]]) < 6:
                        break
        
        c4b[cin][heights[cin]] = 2
        w = win(c4b, heights[cin], cin, 2)
        showboard(c4b)
        if w == 2:
             print("You lost...")
        elif w == 3:
             print("It's a draw.")
             break
        heights[cin] += 1



connect4()