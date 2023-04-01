import os
import time
import ttt
import connect4
import RPS
import checkers
import PythonWrite
import mancala
import hangman
play=True
#defining the functions
def clear(gamename):
    os.system('cls')
    print('Game Catalog >' + gamename +'\n')
#core gameplay loop
x=0
while play==True:
    print('please play this game of tic tac toe twice so that you may understand how to user terminal for our games')
    time.sleep(2)
    ttt.tictactoe()
    ttt.tictactoe()
    gamechoice=int(input('choose a game from the following list by typing its number\n\n1:Tic-Tac-Toe\n2:Connect 4\n3:Rock-Paper-Sciscors\n4:Checkers\n5:Fractal Game\n6:Python Write\n7:Mancala\n8:Hangman\n9:Stop the program\n'))
    if gamechoice==1:
        clear('Tic-Tac-Toe')
        ttt.tictactoe()
    if gamechoice==2:
        clear('Connect 4')
        connect4.connect4()
    if gamechoice==3:
        clear('Rock-Paper-Sciscors')
        RPS.rps()
    if gamechoice==4:
        clear('Checkers')
        checkers.checkers()
    if gamechoice==5:
        clear('fractal game')
        print('god pls help the man who is going to write this code')
    if gamechoice==6:
        clear('Python Write')
        PythonWrite.PythonWrite()
    if gamechoice==7:
        clear('Mancala')
        mancala.mancala()
    if gamechoice==8:
        clear('Hangman')
        hangman.hangman()
    if gamechoice==9:
        break