import os
from random import randint
play=True
#defining the functions
#def clear():
    #os.system('cls')
def tictactoe(): #plan is to make it so that the user input changes the move to an x or an o
    totalmoves=0
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    previousmoves=[]
    usermoves=[]
    compmoves=[]
    print('the following is a sample board with each postion numbered. PLease input a number to make a move\n1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')
    while totalmoves<5:
        playermove=int(input(f'please input your move\nthe following is the board\n{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}\n'))-1
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
    #board variable that is changed based on numbers in a list
    #list that stores the number
    #while loop
    #number that is inputed
    #if statment that checks that the number is already played
    #if not adds to previous move list
    #append the board
    #print the board
    #check for 3 in a row
    #continue is no 3 in a row
def connect4():
    print('working on')
def rps():#plan to make cleaner later
	while True:
		v=0
		movelist=['rock','sciscors','paper','rock']
		compmove=movelist[randint(0,2)]
		rpsmove=input('what is your move Rock or Paper or Sciscors\n').lower()
		for i in movelist:
			if v==1:
				if i==rpsmove:
					  print(f'you went {rpsmove}, computer went {compmove}.\nCongrats you win.\n')
					  break
				else:
					  print(f'you went {rpsmove}, computer went {compmove}.\nI\'m sorry you didn\'t win\n.')
					  break
			if i==compmove:
				v=1
		if input('would you like to play again? y/n\n').lower() == 'n':
			break
def chess():
    print('chess board coming soon')
#core gameplay loop
while play==True:
    gamechoice=int(input('choose a game from the following list by typing its number\n\n1:Tic-Tac-Toe\n2:Connect 4\n3:Rock-Paper-Sciscors\n4:Chess\n5: Fractal Game\n6:Stop the program\n'))
    if gamechoice==1:
        tictactoe()
    if gamechoice==2:
        connect4()
    if gamechoice==3:
        #clear()
        rps()
    if gamechoice==4:
        chess()
    if gamechoice==5:
        print('god pls help the man who is going to write this code')
    if gamechoice==6:
        break
