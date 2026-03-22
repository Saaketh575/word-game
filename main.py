import time
import random
number=0
# for typewriter effect
def typer(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)

def typei(text):
    typer(text)
    user_input = input()
    return user_input

# i roll only 4 dice
def rolldice():
    return [random.randint(1, 6) for kk in range(4)]

# long list of 5 letter words, we must use: with open()
with open("words.txt") as f:
    words = f.read().splitlines()

# Using lambda functions for the operators instead of defining them as one line functions
operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}

# dice is the player's dice
def createlistwords(words, appendlist):
    for kk in range(5):
        appendlist.append(words[random.randint(0, len(words) - 1)])
    return appendlist

# this function is used to create the list of words for the player and the computer
playerwords = []
createlistwords(words, playerwords)

computerwords = []
createlistwords(words, computerwords)

wordpool = []

def computeletter(number):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return letters[number % 26]

def canmakeword(word, pool):
    temppool = pool.copy()
    for letter in word:
        if letter in temppool:
            temppool.remove(letter)
        else:
            return False
    return True

# this function is used to compute the letter from the number
typer('Welcome to Dice Words! The rules are simple: you roll 4 dice, and you must use three operators on the numbers to create a number. We will then show you the letter created by the number, and you can approve or make a different choice of operators. You and the computer will have separate lists of words. If you create a word that is in your list, you win! But a computer will also be playing, and if it creates a word that is in its list, it wins! You will be making the words in the same letter pool, and order of letters doesn\'t matter. Good luck!\n')
typer('To create the letters, we use modulo 26, so these are the base ways to get each letter-if you go higher than 25, you will loop around the alphabet and if you get -1, that will be z. Here is the base. A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11, M=12, N=13, O=14, P=15, Q=16, R=17, S=18, T=19, U=20, V=21, W=22, X=23, Y=24, Z=25.\n')
typer(f'Your words are: {playerwords}\n')

gameover = False

while not gameover:
    dice = rolldice()
    typer(f'You rolled: {dice}\n')
    while True:
        typer('You can use +, -, or *\n')
        typer('You must use 3 operators\n')
        if len(wordpool)>3:
           #give a hint to the player, to make it easier to win
           for word in playerwords:
              hintletters=[letter for letter in word if letter in wordpool] #this list comprehension is used to create a list of letters that are in the word and the word pool, so basically:
   #for letter in word:
      #if letter in wordpool:
         #hintletters.append(letter)
              if len(hintletters)>0:
                 typer(f'Hint: these letters in the word pool will help you make the word {word}: {hintletters}\n')
        operator1 = typei('What is your first operator?\n')
        operator2 = typei('What is your second operator?\n')
        operator3 = typei('What is your third operator?\n')
        
        op1 = operator1.strip()
        op2 = operator2.strip()
        op3 = operator3.strip()
        
        if op1 in operators and op2 in operators and op3 in operators: #this is the check to see if the operators are valid
            if op1 == '+': 
                if op2 == '+':  #this is all the combinations of operators so no matter what the player chooses, it will work
                    if op3 == '+':
                        number = operators['+'](operators['+'](operators['+'](dice[0], dice[1]), dice[2]), dice[3]) #I will twll you what each value of number means, in terms of x, y, z, w
                        #x+y+z+w
                        typer(f'{dice[0]} + {dice[1]} + {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['+'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #x+y+z-w
                        typer(f'{dice[0]} + {dice[1]} + {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['+'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x+y+z)*w
                        typer(f'({dice[0]} + {dice[1]} + {dice[2]}) * {dice[3]}')
                elif op2 == '-':
                    if op3 == '+':
                        number = operators['+'](operators['-'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #x+y-z+w
                        typer(f'{dice[0]} + {dice[1]} - {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['-'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #x+y-z-w
                        typer(f'{dice[0]} + {dice[1]} - {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['-'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x+y-z)*w
                        typer(f'({dice[0]} + {dice[1]} - {dice[2]}) * {dice[3]}')
                elif op2 == '*':
                    if op3 == '+':
                        number = operators['+'](operators['*'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x+y)*z+w
                        typer(f'({dice[0]} + {dice[1]}) * {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['*'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x+y)*z-w
                        typer(f'({dice[0]} + {dice[1]}) * {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['*'](operators['+'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x+y)*z*w
                        typer(f'({dice[0]} + {dice[1]}) * {dice[2]} * {dice[3]}')
            elif op1 == '-':
                if op2 == '+':
                    if op3 == '+':
                        number = operators['+'](operators['+'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #x-y+z+w
                        typer(f'{dice[0]} - {dice[1]} + {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['+'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #x-y+z-w
                        typer(f'{dice[0]} - {dice[1]} + {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['+'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x-y+z)*w
                        typer(f'({dice[0]} - {dice[1]} + {dice[2]}) * {dice[3]}')
                elif op2 == '-':
                    if op3 == '+':
                        number = operators['+'](operators['-'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #x-y-z+w
                        typer(f'{dice[0]} - {dice[1]} - {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['-'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #x-y-z-w
                        typer(f'{dice[0]} - {dice[1]} - {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['-'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x-y-z)*w
                        typer(f'({dice[0]} - {dice[1]} - {dice[2]}) * {dice[3]}')
                elif op2 == '*':
                    if op3 == '+':
                        number = operators['+'](operators['*'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x-y)*z+w
                        typer(f'({dice[0]} - {dice[1]}) * {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['*'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x-y)*z-w
                        typer(f'({dice[0]} - {dice[1]}) * {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['*'](operators['-'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x-y)*z*w
                        typer(f'({dice[0]} - {dice[1]}) * {dice[2]} * {dice[3]}')
            elif op1 == '*':
                if op2 == '+':
                    if op3 == '+':
                        number = operators['+'](operators['+'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y+z+w
                        typer(f'{dice[0]} * {dice[1]} + {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['+'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y+z-w
                        typer(f'{dice[0]} * {dice[1]} + {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['+'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x*y+z)*w
                        typer(f'({dice[0]} * {dice[1]} + {dice[2]}) * {dice[3]}')
                elif op2 == '-':
                    if op3 == '+':
                        number = operators['+'](operators['-'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y-z+w
                        typer(f'{dice[0]} * {dice[1]} - {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['-'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y-z-w
                        typer(f'{dice[0]} * {dice[1]} - {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['-'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #(x*y-z)*w
                        typer(f'({dice[0]} * {dice[1]} - {dice[2]}) * {dice[3]}')
                elif op2 == '*':
                    if op3 == '+':
                        number = operators['+'](operators['*'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y*z+w
                        typer(f'{dice[0]} * {dice[1]} * {dice[2]} + {dice[3]}')
                    elif op3 == '-':
                        number = operators['-'](operators['*'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y*z-w
                        typer(f'{dice[0]} * {dice[1]} * {dice[2]} - {dice[3]}')
                    elif op3 == '*':
                        number = operators['*'](operators['*'](operators['*'](dice[0], dice[1]), dice[2]), dice[3])
                        #x*y*z*w
                        typer(f'{dice[0]} * {dice[1]} * {dice[2]} * {dice[3]}')
            
            letter = computeletter(number)
            typer(f'\nYou can create the letter \'{letter}\'.\n')
            continueornot = typei('Do you want to keep this letter? (y/n)\n')
            if continueornot.strip().lower() == 'y':
                wordpool.append(letter)
                break
            else:
                continue
        else:
            typer('Invalid operators. Please use +, -, or *.\n')  #this is the error message if the player uses an invalid operator
            continue
    # Player word check
    typer(f'The word pool is now: {wordpool} | Recent letters: {wordpool[-3:]}\n')
    typer(f'Your words are: {playerwords}\n')
    for word in playerwords:
        if canmakeword(word, wordpool):
            typer(f'You made the word {word}! You win!\n')
            gameover = True
            break
    if gameover:
       break

    # computer's turn
    typer('The computer is now rolling the dice.\n')
    computerdice = rolldice()
    typer(f'The computer rolled: {computerdice}\n')
    bestword = '' #define bestword
    bestprogress = -1 #it is -1 because if no letters the computer can make, it will not choose a letter beczuse progress is 0 and the statement is if progress > bestprogress
    for word in computerwords: #this is the computer's word check
        progress = 0 #this is the number of letters in the word that are in the word pool
        temppool = wordpool.copy() #this is the word pool that the computer will use to check if it can make the word
        for letter in word: #this is the letter in the word that the computer is checking
            if letter in temppool:
                temppool.remove(letter)#so that the computer doesn't use the same letter twice
                progress += 1 #this adds to the progress of the word so that the computer can choose the best word
        if progress > bestprogress: #this is the computer's check of which word it already has the most progress on
            bestprogress = progress #so if there is a smaller value later on, the computer will not choose that word
            bestword = word         #this is the word that the computer will choose

    temppool = wordpool.copy() #we copy it because we don't want to change the original word pool
    missingletters = []

    for letter in bestword:
        if letter in temppool:
            temppool.remove(letter) #You can't use the same letter twice, unless it appears twice in bestword, so we remove it from the pool
        else:
            missingletters.append(letter)
   #This for loop checks which letters the computer needs to make the word, and adds them to a list of missing letters, by going through every letter in bestword and checking if it is in the word pool. If it is not, it adds it to the list of missing letters.
   
    operatorlist = ['+', '-', '*']
    found_letter = False
    for op1 in operatorlist:
        for op2 in operatorlist:
            for op3 in operatorlist: #three for loops to check all possible combinations of operators
               
                number = operators[op3](operators[op2](operators[op1](computerdice[0], computerdice[1]), computerdice[2]), computerdice[3]) #this is the format that we used for the player, so we brute force all possible combinations of operators using this format
                letter = computeletter(number) #this is the letter that if the computer chooses this combination of operators, it will get        
                
                if letter in missingletters: #checking if it wants this letter
                    wordpool.append(letter)
                    typer(f'The computer added the letter \'{letter}\' to the word pool.\n')
                    typer(f'The word pool is now: {wordpool} | Recent letters: {wordpool[-3:]}\n')
                    found_letter = True
                    break
                
            if found_letter:  #We need all three breaks to break out of all three loops, and found_letter is a flag to check if we found a letter and break through all three loops a bit like broadcast in scratch from loop to loop
               break
               
        if found_letter:
           break
    if not found_letter:
       op1=random.choice(operatorlist)
       op2=random.choice(operatorlist)
       op3=random.choice(operatorlist)
       number=operators[op3](operators[op2](operators[op1](computerdice[0], computerdice[1]), computerdice[2]), computerdice[3]) #if the computer doesn't want any of the letters, it will just choose a random combination of operators
       letter = computeletter(number)
       wordpool.append(letter)
       typer(f'The computer added the letter \'{letter}\' to the word pool.\n')
       typer(f'The word pool is now: {wordpool} | Recent letters: {wordpool[-3:]}\n')
       
    for word in computerwords:
        if canmakeword(word, wordpool):
            typer(f"Computer made {word}! Computer wins!\n")  #this is the computer's win check
            gameover = True
            break
