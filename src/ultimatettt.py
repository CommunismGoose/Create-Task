from random import randint

def win(tb):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for w in wins:
        look = tb[w[0]]
        if look == tb[w[1]] == tb[w[2]]:
            if look != 0:
                return look
    return 0

def playerInput(text, tb):
    pin = 0
    while True:
        pin = input(text + "\n")
        if pin.isnumeric():
            pin = int(pin[0]) - 1
            if pin >= 0 and pin < 9:
                if tb[pin] == 0:
                    break
    return pin

def ultimate_tictactoe(): 
    utb = [[0,0,0,0,0,0,0,0,0]] * 9
    sw = [0,0,0,0,0,0,0,0,0]

    curb = 0
    nexb = 0

    full = True
    while True:
        pin = 0
        if full:
            print()



