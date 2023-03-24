from random import randint
def rps():#plan to make cleaner later
	while True:
		v=0
		movelist=['rock','sciscors','paper','rock']
		compmove=movelist[randint(0,2)]
		rpsmove=input('what is your move Rock or Paper or Sciscors\n').lower()
		for i in movelist:
			if v==1:
				if i==compmove:
					print(f'you went {rpsmove}, computer went {compmove}.\nCongrats you win.\n')
					break
				else:
					print(f'you went {rpsmove}, computer went {compmove}.\nI\'m sorry you didn\'t win\n.')
					break
			if i==rpsmove:
				v=1
		if input('would you like to play again? y/n\n').lower() == 'n':
			break
