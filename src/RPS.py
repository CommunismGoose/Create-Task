from random import randint
def rps():
	while True:
		v=0 #random ahh variable
		movelist=['rock','sciscors','paper','rock'] #possible movess
		compmove=movelist[randint(0,2)] #the computers random move
		rpsmove=input('what is your move Rock or Paper or Sciscors\n').lower() #the user move
		for i in movelist: # for item in possible moves
			if v==1: #if this is the item after usermove
				if i==compmove: #if this move is computer move
					print(f'you went {rpsmove}, computer went {compmove}.\nCongrats you win.\n') 
					break
				else: #if this is a tie or lose
					print(f'you went {rpsmove}, computer went {compmove}.\nI\'m sorry you didn\'t win\n.')
					break
			if i==rpsmove: #if item is usermove
				v=1
		if input('would you like to play again? y/n\n').lower() == 'n': #play again?
			break
