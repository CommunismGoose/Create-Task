#imports modules needed
from wordsz import lotsofwords
from random import randint
import time
#defined the main function that will be called in main.py
def PythonWrite():
    print('This is a typing game in which you get a score based on speed and accuracy')
    highscore={} #list which stores all scores from playthroughs
    while True: #core gameplay loop
        playermove=int(input('Please select one of the following options\n1:Play the Game\n2:View previous scores\n3:quit\n')) 
        if playermove == 1: #if the player wants to play the game
            score=0  #tracks score
            wordsdone=0   #trakcs amount of words given
            while wordsdone<10:#gives words and calcuate scores
                while True:#finds word with length greater 5
                    word=lotsofwords[randint(0,len(lotsofwords))] #gives random word and makes ure it is under 25 characters and above 5
                    if 25>=len(word)>=5:
                        break
                start=int(time.time()) 
                playermove=input(f'Your word is \n{word}\n')
                end=int(time.time())
                placekeeper=0 #keeps index
                for i in word:  #this loop determines how many characters of the typed word are in the right spot
                    if playermove[placekeeper]==i:
                        score+=1 #gives 1 score if the character is correct
                        if placekeeper<len(playermove)-1:
                            placekeeper+=1
                    else:  #removes 1 if character is wrong
                        score-=1
                        if placekeeper<len(playermove)-1:
                            placekeeper+=1
                score-=(end-start)/2 #calcuates the amount of time it took to type in and removes time/2 from score
                wordsdone+=1
            print(f'You got a score of {score}')  #print score, then gets their name and stores it in the dictionary that hold scores
            playername=input('please enter your name\n')
            highscore.update({playername:score})
        if playermove == 2:  #if they want to view scores then we print all the scores
            for i in highscore:
                print(f'\n{i} got a score of {highscore[i]}\n')
        if playermove == 3: #if they want to leave then we break
            break
