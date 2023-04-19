import os
import Blackjack
import connect4
import hangman
import mancala
import minesweeper
import PythonWrite
import RPS
import ttt
from random import randint

#defining the functions
def clear(gamename):
    os.system('cls')
    print('Game Catalog >' + gamename +'\n')

input("First, learn how to use the terminal [enter]")
ttt.tictactoe(False, "x")
ttt.tictactoe(False, "o")

#core gameplay loop
while True:
    clear("")
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
        inp = "x"
        if randint(0,1) == 1:
            inp = "o"
        ttt.tictactoe(True, inp)
    elif gamechoice==2:
        clear('Connect 4')
        connect4.connect4()
    elif gamechoice==3:
        clear('Rock-Paper-Sciscors')
        RPS.rps()
    elif gamechoice==4:
        clear('Pytype')
        PythonWrite.PythonWrite()
    elif gamechoice==5:
        clear('Mancala')
        mancala.mancala()
    elif gamechoice==6:
        clear('Hangman')
        hangman.hangman()
    elif gamechoice==7:
        clear('Blackjack')
        Blackjack.blackjack()
    elif gamechoice==8:
        clear('Minesweeper')
        minesweeper.Minesweeper(12, 12, 0.12)
    else:
        break