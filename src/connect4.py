from random import randint

def win(c4b, x, y, turn):
    adjx = [[-3,-2,-1,0],[-2,-1,0,1],[-1,0,1,2],[0,1,2,3],[3,2,1,0],[2,1,0,-1],[1,0,-1,-2],[0,1,2,3],[0,0,0,0]]
    winx = [0]*3 + [1]*3 + [2]*3 + [3]*3 + [4]*4
    winy = [0,8,4,1,8,5,2,8,6,3,8,7,0,1,2,3]
    print(winx)

    #detect if all board squares are filled, if nobody won it's a draw

def connect4():
    c4b = [[0,0,0,0,0,0]]*7
    heights = [0,0,0,0,0,0,0]

    while True:
        #player move
        pin = -1
        while True:
            pin = input("Pick an available collumn from 1-7: ")
            if pin.isnumeric():
                pin = int(pin) - 1
                if pin >= 0 and pin <= 6:
                    if sum(c4b[pin]) < 6:
                        break
        
        c4b[pin][heights[pin]] = 1
        w = win(c4b, heights[pin], pin, 1)
        if win == 1:
            print("You won!")
            break
        elif win == 3:
            print("It's a draw.")
            break
        heights[pin] += 1

        #computer move



connect4()