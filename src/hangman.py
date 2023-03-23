#import wordsz
from random import randint
import replit
import os
def clear():
    os.system('cls')
    replit.clear()
def stingconv(listz):
    global stringz,hidden
    stringz=''
    for i in listz:
        stringz+=i
def hangman():
    angercount=0
    while True:
        temp=input('Would you like to type your own word in? y/n\n').lower()
        if temp=='y':
            word=input('please type in your word\n').lower()
            if angercount>=3:
                word+=' bruh'
            clear()
            break
        elif temp == 'n':
            print('L cant do this rn')
            break
            #word = lotsofwords[randint(1,len(lotsofwords))]
        else:
            if angercount == 1:
                clear()
                print('bro don\'t make me repeat myself')
            if angercount == 0:
                clear()
                print('please select a valid option')
            if angercount == 2:
                clear()
                print('ay imma keep it straight wit you, i dont think you speak this langauge\n Por favor escribe Y o N')
            if angercount == 3:
                clear()
                print('fam you trippen dawg you already KNOW what i would ask you')
            if angercount == 4:
                clear()
                break
            angercount+=1
    hidden =[]
    wrongletters = ''
    wrong = 0
    numbercorrect=0
    for i in range(len(word)):
        hidden.append('_ ')
    stingconv(hidden)
    print(f'______\n|\n|\n|\nYour word is as follows\n{stringz}')
    while True:
        usermove = input('what letter would you like to guess, you may try to guess the word if you would like\n').lower()
        place = 0
        #for future refrence
        # if len(usermove)>1:
        #     if usermove in word:
                
        if len(usermove)<len(word):
            temp=numbercorrect
            for letter in word:
                if letter == usermove:
                    hidden[place] = letter
                    numbercorrect+=1
                elif numbercorrect==temp and place==len(word)-1:
                    wrongletters += usermove
                    wrong += 1
                place += 1
        else:
            if usermove==word:
                print('you have guessed the correct word')
                if angercount >=2:
                    print('A two yearold could\'ve done that')
                elif 2>angercount>0:
                    print('that was ight')
                break
            else:
                wrong+=1
        if wrong == 0:
            stingconv(hidden)
            print(f'''______\n|\n|\n|\n\n{stringz}\n your wrong letters are as follows\n{wrongletters}''')
        if wrong == 1:
            stingconv(hidden)
            print(f'______\n|   []\n|   \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 2:
            stingconv(hidden)
            print(f'______\n|   [O]\n|   \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong ==3:
            stingconv(hidden)
            print(f'______\n|   [Ow]\n|   \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 4:
            stingconv(hidden)
            print(f'______\n|   [OwO]\n|   \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 5:
            stingconv(hidden)
            print(f'______\n|   [OwO]\n|    / \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 6:
            stingconv(hidden)
            print(f'______\n|   [OwO]\n|    /| \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 7:
            stingconv(hidden)
            print(f'______\n|   [OwO]\n|    /|\ \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if wrong == 8:
            stingconv(hidden)
            print(f'______\n|   [OwO]\n|    /|\ \n|    / \n|\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
        if len(word)>9:
            if wrong == 9:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   \n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
            if wrong == 10:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   o\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
            if wrong == 11:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   o o\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n Your word was{word}\n')
                if angercount >=2:
                    print('Maybe shoul\'ve just type Y or N.... huh')
                break
        else:
            if wrong == 9:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n{stringz}\n your wrong letters are as follows\n{wrongletters}\nyou have failed the game. \n Your word was{word}')
                if angercount >=2:
                    print('Maybe shoul\'ve just type Y or N bruh')
                break
        


        stingconv(hidden)
        if len(stringz)==len(word):
            print('you win')
            if angercount >=2:
                    print('A two yearold could\'ve done that')
            elif 2>angercount>0:
                print('that was ight')
            break
hangman()
