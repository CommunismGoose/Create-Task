import os
#this is a unfinished project that is heavily bugged
mpos=[4,4,4,4,4,4,0,4,4,4,4,4,4,0] #list of values
lsp='               ' #a long space
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
def printboard():
    mboard=(f'    {mpos[12]} {mpos[11]} {mpos[10]} {mpos[9]} {mpos[8]} {mpos[7]}\n {mpos[13]}{lsp}{mpos[6]}\n    {mpos[0]} {mpos[1]} {mpos[2]} {mpos[3]} {mpos[4]} {mpos[5]}\n\n')
    print(mboard)
def mancala():
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
    playerturn=False
    while True:
        playerturn=not playerturn
        print(playerturn)
        printboard()
        if playerturn==True:
            while True:
                usermove=int(input('please input your move, 1 to 6 starting bottom left going counter clockwise\n'))-1#gets pos of move
                if usermove>5 or mpos[usermove]==0:
                    print('please select a valid option\n')
                else:
                    break
            if usermove<6 and mpos[usermove]!=0: #if the move is legal
                temp=mpos[usermove]#temp variable is set to the position
                mpos[usermove]=0
                i=usermove+1
                while temp!=0:#while hand isnt equal to zero
                    if i!=13: #if pos isnt 13
                        temp-=1 #amount in hands minus
                        mpos[i]+=1 #amount in position plus
                        print(f'add1, {temp} left in hand')
                        printboard()
                    if temp==0 and i!=13 and i!=6 and mpos[i]>1: 
                        #if head is equal to zero, and we are no tin endgoal and current pos value is not zero
                        temp=mpos[i] #hand equal value in square
                        mpos[i]=0 #square value = 0
                        print(f'pickup {temp} amount')
                        printboard()
                    i+=1 #current pos 1 higher
                    if i==14: #if current pos is out of index
                        i=0 #equal it to zero
                        print('reset')
        while True:
            if playerturn==False:
                while True:
                    usermove=int(input('please input your move, 7 to 12 starting bottom left going counter clockwise\n'))#gets pos of move
                    if usermove<7 or mpos[usermove]==0:
                        print('please select a valid option\n')
                    else:
                        break
                if usermove>6 and mpos[usermove]!=0: #if the move is legal
                    temp=mpos[usermove]#temp variable is set to the position
                    mpos[usermove]=0
                    i=usermove+1
                    print('test 1')
                    while temp!=0:#while hand isnt equal to zero
                        print('test 2')
                        if i!=6: #if pos isnt 6
                            temp-=1 #amount in hands minus
                            mpos[i]+=1 #amount in position plus
                            print(f'add1, {temp} left in hand')
                            printboard()
                        if temp==0 and i!=13 and i!=6 and mpos[i]>1: 
                            #if head is equal to zero, and we are no tin endgoal and current pos value is not zero
                            temp=mpos[i] #hand equal value in square
                            mpos[i]=0 #square value = 0
                            print(f'pickup {temp} amount')
                            printboard()
                        i+=1 #current pos 1 higher
                        if i==14: #if current pos is out of index
                            i=0 #equal it to zero
                            print('reset')
                    if temp==0:
                        break
mancala()
