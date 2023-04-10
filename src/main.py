import os
import time
import ttt
import connect4
import RPS
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
    print("Choose a game from the following list by typing its number.\n")
    print("1: Tic-tac-toe")
    print("2: Connect 4")
    print("3: Rock-paper-scissors")
    print("4: Python Write")
    print("5: Mancala")
    print("6: Hangman")
    print("7: Blackjack")
    print("8: Minesweeper")
    print("9: End program")
    gamechoice=int(input())
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
        clear('Python Write')
        PythonWrite.PythonWrite()
    if gamechoice==5:
        clear('Mancala')
        mancala.mancala()
    if gamechoice==6:
        clear('Hangman')
        hangman.hangman()
    if gamechoice==7:
        break