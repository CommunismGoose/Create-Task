import os
import time
mpos=[4,4,4,4,4,4,0,4,4,4,4,4,4,0] #list of values
lsp='               ' #a long space
def clear(gamename):
    time.sleep(.6)
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
def printboard():
    mboard=(f'    {mpos[12]} {mpos[11]} {mpos[10]} {mpos[9]} {mpos[8]} {mpos[7]}\n {mpos[13]}{lsp}{mpos[6]}\n    {mpos[0]} {mpos[1]} {mpos[2]} {mpos[3]} {mpos[4]} {mpos[5]}\n\n')
    print(mboard)
wins=False
def wincheck():
    global wins
    if mpos[12]+mpos[11]+mpos[10]+mpos[9]+mpos[8]+mpos[7]==0 or mpos[0]+mpos[1]+mpos[2]+mpos[3]+mpos[4]+mpos[5]==0 or mpos[6]>=25 or mpos[13]>=25 :
        wins=True
        if wins==True:
            print(f'game has ended with player 1 ending with {mpos[6]} and player 2 ending with {mpos[13]} ')
            if mpos[13]>mpos[6]:
                print('Player 2 wins!')
            elif mpos[13]==mpos[6]:
                print('Tie!')
            else:
                print('Player 1 wins!')
def leaving():
    global leave
    if leave:
        break
def mancala():
    input('''The rules are as follows
    1:You\'re starting move may only be on your side of the board
    2:You must drop a piece into every hole/square that you pass over.
    3:If the hole that you drop your last piece into has pieces in it you must pick it up and continue
    4:You cannot drop a piece into the enemy's goal
    5:If you drop your final piece into your goal on the end you gain another turn
    6:You win if you have the most pieces in your goal at the end of the game
    7:The game ends if the board meets any of these conditions: There are no possible moves for one of the players, All the pieces on the board are in endgoals, or If the a draw is agreed upon.
    Type ok when you understand
    ''')
    leave=False
    playerturn=False
    while True:
        wincheck()
        if wins==True:
            break
        playerturn=not playerturn
        clear('Mancala')
        printboard()
        anothermove=True
        while anothermove==True:
            anothermove=False
            if playerturn==True:
                while True:
                    usermove=int(input('PLAYER 1:please input your move, 1 to 6 starting bottom left going counter clockwise\nYou may also type 0 to quit\n'))-1#gets pos of move
                    if usermove==-1:
                        leave=True
                        break
                    if usermove>5 or mpos[usermove]==0:
                        print('please select a valid option\n')
                    else:
                        break
                leaving()
                if usermove<6 and mpos[usermove]!=0: #if the move is legal
                    temp=mpos[usermove]#temp variable is set to the position
                    mpos[usermove]=0
                    i=usermove+1
                    while temp!=0:#while hand isnt equal to zero
                        if i!=13: #if pos isnt 13
                            temp-=1 #amount in hands minus
                            mpos[i]+=1 #amount in position plus
                            clear('Mancala')
                            printboard()
                        if temp==0 and i!=13 and i!=6 and mpos[i]>1: 
                            #if head is equal to zero, and we are no tin endgoal and current pos value is not zero
                            temp=mpos[i] #hand equal value in square
                            mpos[i]=0 #square value = 0
                            clear('Mancala')
                            printboard()
                        if temp==0 and i==6:
                            anothermove=True
                            wincheck()
                            if wins==True:
                                break
                        i+=1 #current pos 1 higher
                        if i==14: #if current pos is out of index
                            i=0 #equal it to zero
        anothermove=True
        leaving()
        while anothermove==True:
            anothermove=False
            if playerturn==False:
                while True:
                    usermove=int(input('PLAYER 2: please input your move, 7 to 12 starting bottom left going counter clockwise\nYou may type 0 to leave\n'))#gets pos of move
                    if usermove==0:
                        leave=True
                        break
                    if usermove<7 or mpos[usermove]==0:
                        print('please select a valid option\n')
                    else:
                        break
                if usermove>6 and mpos[usermove]!=0: #if the move is legal
                    temp=mpos[usermove]#temp variable is set to the position
                    mpos[usermove]=0
                    i=usermove+1
                    while temp!=0:#while hand isnt equal to zero
                        if i!=6: #if pos isnt 6
                            temp-=1 #amount in hands minus
                            mpos[i]+=1 #amount in position plus
                            clear('Mancala')
                            printboard()
                        if temp==0 and i!=13 and i!=6 and mpos[i]>1: 
                            #if head is equal to zero, and we are no tin endgoal and current pos value is not zero
                            temp=mpos[i] #hand equal value in square
                            mpos[i]=0 #square value = 0
                            clear('Mancala')
                            printboard()
                        if temp==0 and i==13:
                            anothermove=True
                            wincheck()
                            if wins==True:
                                break
                        i+=1 #current pos 1 higher
                        if i==14: #if current pos is out of index
                            i=0 #equal it to zero
                leaving()
mancala()