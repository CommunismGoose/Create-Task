import os
from random import randint
#clear function
def clear(gamename):
    os.system('cls')
    print(f'Game Catalog > {gamename}\n')
#determines a loss from going over 21 and makes aces worth less if you do go over, also just gives you a card
def calcvalue(theguy):
    global playerhand, dealerhand, totalvalue
    acestorage=[]
    totalvalue=0
    for i in theguy: 
        if i == 11:
            acestorage.append(i) #if there is an ace saves the index of it
        totalvalue+=i  #calcuates the total value of their hand
def hit(whomoving):
    #defining variables
    global cards, playerhand, dealerhand, totalvalue
    acestorage=[]
    whomoving.append(cards[randint(0,51)])#give them a new card
    calcvalue(whomoving)
    if totalvalue>21:  #if their hand is bust
        if len(acestorage)>0:  #if they have an ace in their hand change it to a 1
            for i in acestorage:
                playerhand[i]==1
                totalvalue-=10
                if totalvalue<21: #only changes as many aces as is needed
                    break
    if totalvalue<=21: #if they hand isnt bust
        return False  #else they still in play with one new card
    else:
        return True  #they lose and we return true
def blackjack(): 
    global cards, playerhand, dealerhand
    #defining variables
    cards=[]
    playerhand=[]
    dealerhand=[]
    cards=[]
    nomark=''
    onemark=' ?'
    #Creating a list of all cards
    for i in range (1,11):
        i+=1
        if i==10:
            for u in range(16):
                cards.append(i)
        if i!=10:
            for u in range(4):
                cards.append(i)
    #Adding cards into player's hand
    for i in range(2):
        playerhand.append(cards[randint(0,51)])
        dealerhand.append(cards[randint(0,51)])
    #core gameplay loop
    while True:
        usermove=input(f'Your hand is {playerhand}\nand the dealers hand is {dealerhand[0]}{onemark if len(dealerhand)>2 else nomark} ?\nIf you would like to hit please type \'Hit\'\nIf you would like to stand please type \'Stand\'\n').lower()
        clear('21 Blackjack')
        if usermove=='hit':
            if hit(playerhand): #if they bust
                print(f'Im sorry you have lost with {playerhand} against the dealers {dealerhand}')
                break
        calcvalue(dealerhand)
        if totalvalue<17: #if the dealer hits
            print('\nThe dealer has chosen to hit\n')
            if hit(dealerhand): #if they bust
                print(f'You win, The dealer has lost with {dealerhand}')
                break
        else: #if they stand
            print('the dealer has chosen to stand.')
            if usermove=='stand': #if both stand
                calcvalue(playerhand)
                playervalue=totalvalue
                calcvalue(dealerhand)
                dealervalue=totalvalue
                if playervalue>dealervalue: #theese if statments just calc who wins
                    print(f'You have won with the hand {playerhand} vs the dealers {dealerhand}')
                elif playervalue==dealervalue:
                    print(f'You and the dealer have tied with the hands {playerhand}, {dealerhand}')
                else:
                    print(f'You have lost with the hand {playerhand} vs the dealer\'s {dealerhand}')
                break
