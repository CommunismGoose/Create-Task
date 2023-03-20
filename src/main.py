play=True
#defining the functions
def tictactoe():
    print(f' | | \n-----\n | | \n-----\n | | ')
def connect4():
    print('working on')
def rps():
    print('ez')
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
