from wordsz import lotsofwords
from random import randint
import time
def PythonWrite():
    #Ask to play game or view scores
    #if view scores then print saved scores
    #if play game assign a random word over length of 5
    #time how long it takes for word to be inputed
    #score is length of word+4-seconds-number of wrong letters it takes to write word
    #does this for 10 rounds
    #score is all the scores combined
    #add score to hgih score sections, could be a dictionary or list
    #repeat
    print('This is a typing game in which you get a score based on speed and accuracy')
    highscore={}
    while True:
        playermove=int(input('Please select one of the following options\n1:Play the Game\n2:View previous scores\n3:quit\n'))
        if playermove == 1:
            score=0
            wordsdone=0
            while wordsdone<10:#gives words and calcuate scores
                while True:#finds word with length greater 5
                    word=lotsofwords[randint(0,len(lotsofwords))]
                    if 20>=len(word)>=5:
                        break
                start=int(time.time())
                playermove=input(f'Your word is \n{word}\n')
                end=int(time.time())
                placekeeper=0
                for i in word:
                    if playermove[placekeeper]==i:
                        score+=1
                        if placekeeper<len(playermove)-1:
                            placekeeper+=1
                    else:
                        score-=1
                        if placekeeper<len(playermove)-1:
                            placekeeper+=1
                score-=(end-start)/2
                wordsdone+=1
            print(f'You got a score of {score}')
            playername=input('please enter your name\n')
            highscore.update({playername:score})
        if playermove == 2:
            for i in highscore:
                print(f'{i} got a score of {highscore[i]}\n\n\n')
        if playermove == 3:
            break
PythonWrite()