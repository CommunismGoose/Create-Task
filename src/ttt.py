from random import randint
import os
import time
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
winningcombos=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
usermoves=[]
computermoves=[]
def wincheck():
    global usermoves,computermoves,u,o
    for i in winningcombos:
        u=0;o=0
        for b in i:
            if b in usermoves:
                u+=1
            if b in computermoves:
                o+=1
        if u==2:
            print('You win!')
            break
        if o==2:
            print('Computer wins!')
            break
def tictactoe():
    global usermoves,computermoves
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    allmoves=[]
    totalmoves=0
    while True:
        playermove=int(input(f'please input your move\nthe following is the board\n{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}\n'))-1
        if playermove not in allmoves:
            usermoves.append(playermove)
            board[playermove]='X'
            totalmoves+=1
            wincheck()
            if u>=2:
                break
            if totalmoves==9:
                print('Tie')
            while True:
                compmove=randint(0,8)
                if compmove not in allmoves:
                    computermoves.append(compmove)
                    board[compmove]='O'
                    if u>=2:
                        break
        else:
            print('please select a valid move!')
tictactoe()