#9 letter word game

import random
from random import shuffle
from itertools import permutations
from collections import Counter

     
def main():
    infile = open('words_list','r')
    wordlist = infile.readlines()
##    for i in range(len(wordlist)):
##        print(wordlist[i])

    nine_letter_list = [] #initialise 9 letter word list
    for i in range(len(wordlist)):
        if len(wordlist[i]) == 10: #check len
##            print(wordlist[i])
            nine_letter_list.append(wordlist[i])
##    print(nine_letter_list)

    print('-'*50)
    print('   WELCOME TO GAME')
    print('-'*50)
    playerinput = input('Start New game? (Y/N):  ')
    print('-'*50)
    if playerinput[0] == 'Y' or playerinput[0] == 'y':
##        print('Yes')
        newword = random.choice(nine_letter_list) #get random 9 let word from list
        print('Word is:', newword[:-1])
        print('-'*50)
        shuffled = list(newword)
##        print(shuffled)
        shuffled = shuffled[:-1] #remove \n
        random.shuffle(shuffled)
        shuffled_word = ''.join(shuffled)
        shuffled_word = shuffled_word.lower()
##        print(type(shuffled_word))
        print("Word when shuffled: ", shuffled_word)
        print('-'*50)
        print( 'Here is 3X3 matrix of word:')
        print('   ',shuffled_word[0], '   ',shuffled_word[1], '   ',shuffled_word[2])
        print('   ',shuffled_word[3], '   ',shuffled_word[4], '   ',shuffled_word[5])
        print('   ',shuffled_word[6], '   ',shuffled_word[7], '   ',shuffled_word[8])

        #remove \n in wordlist
        wordlist2 = [line.rstrip('\n') for line in wordlist]
##        print(wordlist2)
        

        stop_try = False
        print('-'*50)
        userscore = 0 #ititalise user point score counter
        totalscore = 0 #initialise total score possible
        answerlist = [] #initialise list to put in all correct answers
        lenword = len(shuffled_word) #get length of shuffled
        counterword = Counter(shuffled_word) #counter function
        print('counter of letters in word is', counterword)
        print('User score is 0')

        #get answerkey (with repreating letters)
        
        for i in range(len(wordlist2)):
            if len(wordlist2[i]) < 4: # check length less than 3
                pass #break or pass?
            else:
                for j in range(len(wordlist2[i])):
##                    print(wordlist2[i][j])
                    if wordlist2[i][j] not in shuffled_word:
                        break
                    else:
                        if j+1 == len(wordlist2[i]): #check if last element
                            answerlist.append(wordlist2[i])

        answerlistfinal = []
##        print('counterword is',counterword)
##        print('answerlist is',answerlist)
        for word in answerlist:
##            print(word)
            wordcount = Counter(word)
            loopcount = 0
##            print(wordcount)
            for letter in wordcount:
                loopcount+= 1
                ##                print('loopcount is',loopcount)
                if wordcount[letter] <= counterword.get(letter):
                    if loopcount == len(wordcount):
##                        print('yes')
                        answerlistfinal.append(word)
                else:
                    loopcount = 0
                
        print('answerlist is',answerlistfinal)
            
                            
        #get maxscore
        maxscore = 0
        for word in answerlistfinal:
            for letter in range(len(word)):
                maxscore+=1
            

                
        #checking if user answer is correct
        useranswerlist = []
        while not stop_try:
            userinput = input('What is the answer? (XXX to stop): ')
            if userinput[0] == 'X' or userinput[0] == 'x':
                print("Your score is:", userscore, "Thanks for playing")
                break
            else:
                print('Max score possible is',maxscore)
                if userinput in answerlistfinal:
                    if userinput not in useranswerlist:
                        print("your answer is in the word: ", newword)
                        userscore += len(userinput)
                        useranswerlist.append(userinput)
                        print('Total score so far is: ', userscore)
                    else:
                        print('You have already submitted this word')
                else:
                    print('Your answer is not in the given word: ', newword)                   
            
main()
 
def main4():
    wordlist = ['b','bb','become',]
    word = 'ccolumbine'
    answer = []
    answer2 = []
    print('wordlist is' , wordlist)
    print('word is' , word)

##    dict1 = {'a':1,'b':3,'c':6}
##    print(dict1.keys()[-1])

    #get count of every letter
    shufflecount = Counter(word)
    print(shufflecount)
    print(shufflecount.keys())

    for i in range(len(wordlist)):
        wordcount = Counter(wordlist[i])
##        print('wordcount is',wordcount)
        for j in range(len(wordlist[i])):
            if wordlist[i][j] not in word:
                break
            else:
                if j+1 == len(wordlist[i]): #checking for last element
##                    print('shufflecount is',shufflecount)
                    answer.append(wordlist[i]) #all correct letters are inside

##    print(answer)
                

    for i in range(len(wordlist)):
        wordcount = Counter(wordlist[i])
        for key in wordcount:
            print(key)
            print('shufflecount key',shufflecount.get(key))
            if wordcount[key] <= shufflecount.get(key):
##                if wordcount[key] == wordcount.keys()[-1]: #check last element from list of keys
                answer2.append(wordlist[i])
        
    print(answer2)
##main4()

    
def main5():
    dict1 = {'A':5,'B':10,'C':15}
    dict2 = {'A':10,'B':20,'F':9,'D':15,'C':20}
##    print('return value : %d' % cmp(dict1,dict2))
    count = 0
    for i in dict1:
        count+=1
##        print(dict2.get(i))
        if dict1[i] <= dict2.get(i):
            if count == len(dict1):
                print('yes')

    list1 = ['a','bc','bcde']
    total = 0
    for i in list1:
        for j in range(len(i)):
            total += 1
    print(total)
    
##main5()
    







