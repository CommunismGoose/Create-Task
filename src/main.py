import os
from ttt import *
from connect4 import *
from RPS import *
from checkers import *
from PythonWrite import *
from mancala import *
play=True
#defining the functions
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
#core gameplay loop
while play==True:
    clear('')
    gamechoice=int(input('choose a game from the following list by typing its number\n\n1:Tic-Tac-Toe\n2:Connect 4\n3:Rock-Paper-Sciscors\n4:Checkers\n5: Fractal Game\n6:Python Write\n7:Mancala\n8:Stop the program\n'))
    if gamechoice==1:
        clear('Tic-Tac-Toe')
        tictactoe()
    if gamechoice==2:
        clear('Connect 4')
        connect4()
    if gamechoice==3:
        clear('Rock-Paper-Sciscors')
        rps()
    if gamechoice==4:
        clear()
        checkers()
    if gamechoice==5:
        clear('Checkers')
        print('god pls help the man who is going to write this code')
    if gamechoice==6:
        clear('Python Write')
        PythonWrite()
    if gamechoice==7:
        clear()
        mancala()
    if gamechoice==8:
        break