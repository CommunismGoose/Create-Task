import os
#this is a unfinished project that is heavily bugged
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
def mancala():
    mpos=[4,4,4,4,4,4,0,4,4,4,4,4,4,0] #list of values
    lsp='               ' #a long space
    mboard=(f'    {mpos[0]} {mpos[1]} {mpos[2]} {mpos[3]} {mpos[4]} {mpos[5]}\n {mpos[6]}{lsp}{mpos[13]}\n    {mpos[7]} {mpos[8]} {mpos[9]} {mpos[10]} {mpos[11]} {mpos[12]}')
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
        temp=mpos[usermove]#temp is the value of the hole the user picked up
        mpos[usermove]=0#we reset the beads in the hole user picked up to zero
        i=usermove
        bug=0
        while temp!=0: #while the user has beads in they hands
            if i>13:
                i=0
            if i!=13:#if our current postion is not 13
                i+=1   #updates current position
                temp-=1   #the amount in our hand
                mpos[i]+=1   #adds 1 to the hole
            else: #skips 13th hole
                i+=1 #skips 13th
            if temp==0 and i!=6:  #if we are out of beads
                if mpos[i]!=0:
                    temp=mpos[i] #makes our beads equal to the amount of beads in the hole
                    mpos[i]=0 #removes the beads in the hole essentially we just picked up the beads
            print(i,temp,mpos)
            bug+=1
            if bug == 100:
                break
        print('bye')
    print('why')
