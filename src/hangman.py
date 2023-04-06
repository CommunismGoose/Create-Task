from wordsz import *
from random import randint
import os
def clear(): #clear function
    os.system('cls')
def stingconv(listz): #concatanates list
    global stringz,hidden
    stringz=''
    for i in listz:
        stringz+=i
def hangman():  #main function
    while True: #gets a valid option for if the user wants to type in their own word or get a random one
        temp=input('Would you like to type your own word in? y/n\n').lower()
        if temp=='y':
            word=input('please type in your word\n').lower()
            clear()
            break
        elif temp == 'n':
            word = lotsofwords[randint(1,len(lotsofwords))]
            break
        else:
            clear()
            print('please select a valid option')
    hidden =[] #what is displayed as blank that we still gotta guess
    wrongletters = '' #letters that have been guessed that are wrongn
    wrong = 0  #wrong amount
    numbercorrect=0  #right amount
    for i in range(len(word)): #creates the hidden list
        hidden.append(' _ ')
    stingconv(hidden)  #makes the list into a string
    print(f'______\n|\n|\n|\nYour word is as follows\n{stringz}')  #prints the hidden word
    while True:
        usermove = input('what letter would you like to guess, you may try to guess the word if you would like\n').lower() #gets the letter user guesses
        place = 0  #current index
        if len(usermove)<len(word): #if the lengeth of usermove is less then the length of the word
            temp=numbercorrect #number incorrect is assigned a temp variable
            for letter in word:  #for every letter in the word
                if letter == usermove: #if the currennt letter is equal to usermove then replace the index in hidden with the correct letter
                    hidden[place] = letter  
                    numbercorrect+=1
                elif numbercorrect==temp and place==len(word)-1: #else if the number correct is equal to tempoary variable and the place is on the last letter
                    wrongletters += usermove #we add this as a wrong letter
                    wrong += 1
                place += 1
        else:  #if the lengeth of user move is equal to or greater then the length of the word
            if usermove==word: #if they guessed the right the word
                print('you have guessed the correct word')
                break
            else: #if they didnt guess the right word
                wrong+=1
        if wrong == 0: #this and the following like 20 lines of code are just printing all the possible states of the hangman, im sure i couldve done it with if else statments but that wouldve looked somehow worse and taken only a few less lines of code
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
        if len(word)>9: #this one givs more attempts if the word is long
            if wrong == 9:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   \n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
            if wrong == 10:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   o\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n')
            if wrong == 11:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n|   o o\n{stringz}\n your wrong letters are as follows\n{wrongletters}\n Your word was {word}\n')
                break # man got hung
        else:
            if wrong == 9:
                stingconv(hidden)
                print(f'______\n|   [OwO]\n|    /|\ \n|    /\ \n{stringz}\n your wrong letters are as follows\n{wrongletters}\nyou have failed the game. \n Your word was {word}')
                break #ma got hung
        stingconv(hidden)
        if len(stringz)==len(word): #if they won
            print('you win')
            break
