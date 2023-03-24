from random import randint
import os
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
def tictactoe(): #plan is to make it so that the user input changes the move to an x or an o
    totalmoves=0
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    previousmoves=[]
    usermoves=[]
    compmoves=[]
    print('the following is a sample board with each postion numbered. PLease input a number to make a move\n1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')
    while totalmoves<5:
        playermove=int(input(f'please input your move\nthe following is the board\n{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}\n'))-1
        clear('Tic-Tac-Toe')
        if playermove not in previousmoves:
            previousmoves.append(playermove)
            usermoves.append(playermove)
            board[playermove]='x'
            totalmoves+=1
            while True:
                computermove=randint(0,8)
                if totalmoves==5:
                    break
                if computermove not in previousmoves:
                    previousmoves.append(computermove)
                    compmoves.append(computermove)
                    board[computermove]='o'
                    break
        else:
            print('that is not a legal move go again')
