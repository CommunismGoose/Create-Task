from random import randint
from os import system

def clear(text):
     system("cls")
     print("Game Catalog > " + text)

def win(c4b):
    #horizontal check
    for y in range(6):
        counter = 1
        check = c4b[0][y]
        for x in range(1,7):
            current = c4b[x][y]
            if current == check:
                counter += 1
                if counter == 4:
                    if check != 0:
                         return check 
            else:
                counter = 0
                check = current
        
    #vertical
    for x in range(7):
        counter = 1
        check = c4b[x][0]
        for y in range(1, 6):
            current = c4b[x][y]
            if current == check:
                counter += 1
                if counter == 4:
                    if check != 0:
                         return check 
            else:
                counter = 0
                check = current
             
            
              


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

    clear("Connect 4")
    showboard(c4b)

    turn = 1
    while True:
        pin = 0

        if turn == 1:
            #player move
            while True:
                pin = input("Pick an available collumn from 1-7: ")
                if pin.isnumeric():
                    pin = int(pin) - 1
                    if pin >= 0 and pin <= 6:
                        if sum([x!=0 for x in c4b[pin]]) < 6:
                            break
        elif turn == 2:
            #computer move
            while True:
                pin = randint(0, 6)
                if sum([x!=0 for x in c4b[pin]]) < 6:
                            break

        c4b[pin][heights[pin]] = turn
        heights[pin] += 1

        clear("Connect 4")
        showboard(c4b)

        w = win(c4b)
        if w == 1:
            print("You won!")
            break
        elif w == 3:
            print("It's a draw.")
            break
        elif w == 2:
            print("You lost...")
            break

        turn = (2 if (turn == 1) else 1)

connect4()