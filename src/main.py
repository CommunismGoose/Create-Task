import os
from RPS import *
rps()
play=True
#defining the functions
def clear():
    os.system('cls')
def connect4():
    print('working on')

def checkers():
    print('chess board coming soon')
#core gameplay loop
while play==True:
    gamechoice=int(input('choose a game from the following list by typing its number\n\n1:Tic-Tac-Toe\n2:Connect 4\n3:Rock-Paper-Sciscors\n4:Checkers\n5: Fractal Game\n6:Stop the program\n'))
    if gamechoice==1:
        ttt.tictactoe()
    if gamechoice==2:
        connect4()
    if gamechoice==3:
        #clear()
        rps()
    if gamechoice==4:
        checkers()
    if gamechoice==5:
        print('god pls help the man who is going to write this code')
    if gamechoice==6:
        break
