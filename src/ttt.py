from random import randint
import os

#clear terminal and print the currect game
def clear():
    os.system("cls")
    print("Game Catalog > Tic-Tac-Toe\n\n")

#display the tic tac toe board to the user
def showtttboard(tttboard, pside):
    clear()
    disp = [" ","X","O"] if pside else [" ", "O", "X"]
    cb = [disp[x] for x in tttboard]
    print(" "+cb[0]+" | "+cb[1]+" | "+cb[2])
    print("-----------")
    print(" "+cb[3]+" | "+cb[4]+" | "+cb[5])
    print("-----------")
    print(" "+cb[6]+" | "+cb[7]+" | "+cb[8] + "\n")

def win(tb, turn, pside):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        if turn == tb[w[0]] == tb[w[1]] == tb[w[2]]:
            if turn == 1:
                clear()
                showtttboard(tb, pside)
                print("You won!\n")
                return 1
            elif turn == 2:
                clear()
                showtttboard(tb, pside)
                print("You lost...\n")
                return 1

    if not 0 in tb:
        clear()
        showtttboard(tb, pside)
        print("It's a draw.\n")
        return 1

    showtttboard(tb, pside)
    return 0

#play tic tac toe
def tictactoe(pa, side):
    pside = side == "x"
    tn = 1 if pside else 2

    playagain = True
    while playagain:
        ticb = [0,0,0,0,0,0,0,0,0]
        showtttboard(ticb, pside)

        turn = tn
        #game loop
        while True:
            pin = 0

            if turn == 1: #player move
                while True:
                    pin = input("Where? (1 - 9)\n")
                    if pin.isnumeric():
                        pin = int(pin[0]) - 1
                        if pin >= 0 and pin < 9:
                            if ticb[pin] == 0:
                                break
            else: #computer move
                while True:
                    pin = randint(0, 8)
                    if ticb[pin] == 0:
                        break          

            ticb[pin] = turn
            if win(ticb, turn, pside) == 1:
                input("[enter]")
                break
            
            turn = 2 if turn == 1 else 1

        if pa:
            playagain = input("Play again?\n").lower() in ["y", "yes"]
        else:
            break
