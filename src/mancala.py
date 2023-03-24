import os
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
def mancala():
    global mboard, mpos
    mpos=[0,4,4,4,4,4,4,4,4,4,4,4,4,0]
    longspace='               '
    mboard=(f'    {mpos[1]} {mpos[2]} {mpos[3]} {mpos[4]} {mpos[5]} {mpos[6]}\n {mpos[0]}{longspace}{mpos[13]}\n    {mpos[7]} {mpos[8]} {mpos[9]} {mpos[10]} {mpos[11]} {mpos[12]}')
    print('''The rules are as follows
    1:You\'re starting move may only be on your side of the board
    2:You must drop a piece into every hole/square that you pass over.
    3:If the hole that you drop your last piece into has pieces in it you must pick it up and continue
    4:You cannot drop a piece into the enemy's goal
    5:If you drop your final piece into your goal on the end you gain another turn
    6:You win if you have the most pieces in your goal at the end of the game
    7:The game ends if the board meets any of these conditions: There are no possible moves for one of the players, All the pieces on the board are in endgoals, or If the a draw is agreed upon.
    ''')
    while True:
        print(mboard)
        usermove=int(input('please input your move, 1 to 6 starting bottom left going counter clockwise'))
        if usermove
os.system('pause')
