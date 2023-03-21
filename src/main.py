import os
from random import randint
play=True
#defining the functions
def clear():
    os.system('cls')
def tictactoe():
    print(f' | | \n-----\n | | \n-----\n | | ')
def connect4():
    print('working on')
def rps():#plan to make cleaner later
	while True
		v=0
		movelist=['rock','sciscors','paper','rock']
		compmove=movelist[randint(0,2)]
		rpsmove=input('what is your move Rock or Paper or Sciscors").lower()
		for i in movelist:
			if v==1:
				if i==rpsmove:
					  print(f'you went {rpsmove}, computer went{compmove}.\nCongrats you win.')
					  break
				else:
					  print(f'you went {rpsmove}, computer went{compmove}.\nI\'m sorry you lose.')
					  break
			if i==compmove:
				v=1
		if input('would you like to play again? y/n').lower() == 'n':
			Break
def chess():
    print('chess board coming soon')
#core gameplay loop
while play==True:
    gamechoice=int(input('choose a game from the following list by typing its number\n\n1:Tic-Tac-Toe\n2:Connect 4\n3:Rock-Paper-Sciscors\n4:Chess\n5: Fractal Game'))
    if gamechoice==1:
        tictactoe()
    if gamechoice==2:
        connect4()
    if gamechoice==3:
        rps()
    if gamechoice==4:
        chess()
    if gamechoice==5:
        print('god pls help the man who is going to write this code')
