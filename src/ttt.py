from random import randint
import os

#clear terminal and print the currect game
def clear():
    os.system("cls")
    print("Game Catalog > Tic-Tac-Toe\n\n")

#display the tic tac toe board to the user
def showtttboard(tttboard):
    clear()
    cb = [[" ","X","O"][x] for x in tttboard]
    print(" "+cb[0]+" | "+cb[1]+" | "+cb[2])
    print("-----------")
    print(" "+cb[3]+" | "+cb[4]+" | "+cb[5])
    print("-----------")
    print(" "+cb[6]+" | "+cb[7]+" | "+cb[8] + "\n")

#detect if and who won for any board state tb
def win(tb):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        look = tb[w[0]]
        if look == tb[w[1]] == tb[w[2]]:
            if look != 0:
                return look
    return 0

#play tic tac toe
def tictactoe():
    playagain = True
    while playagain:
        ticb = [0,0,0,0,0,0,0,0,0]
        showtttboard(ticb)

        #game loop
        while True:
            pin = 0
            
            #user input
            while True:
                pin = input("Where? (1 - 9)\n")
                if pin.isnumeric():
                    pin = int(pin[0]) - 1
                    if pin >= 0 and pin < 9:
                        if ticb[pin] == 0:
                            break

            ticb[pin] = 1
            showtttboard(ticb)
            if win(ticb) == 1:
                print("You won!")
                break
            if not 0 in ticb:
                print("It's a draw!")
                break
            
            #computer's move (random)
            cin = pin
            while ticb[cin] != 0:
                cin = randint(0,8)
            
            ticb[cin] = 2
            showtttboard(ticb)
            if win(ticb) == 2:
                print("You lost...")
                break

        playagain = input("Play again?\n").lower() in ["y", "yes"]

#tictactoe()
