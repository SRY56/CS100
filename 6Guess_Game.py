# Shailesh Yannam
# cs 100 2023S section 012
# HW 06, March 22, 2023

# Problem 1
def twoWords(number, letter):
    words = []
    while True:
        ask = input("Enter a "+str(number)+"-letter word: ")
        if len(ask) == number:
            words.append(ask)
            break
    
    while True:
        ask2 = input("Enter a word beginning with "+str(letter)+" please: ")
        if ask2[0].lower() == letter.lower():
            words.append(ask2)
            break
    return words

print(twoWords(9, 'K'))

print()

#Problem 2
def twoWordsV2(number, letter):
    words = []
    x = True
    while x:
        ask = input("Enter a "+str(number)+"-letter word: ")
        if len(ask) == number:
            words.append(ask)
            x = False
    y = True
    while y:
        ask2 = input("Enter a word beginning with "+str(letter)+" please: ")
        if ask2[0].lower() == letter.lower():
            words.append(ask2)
            y = False
    return words

print(twoWordsV2(10, 'A'))

print()

#Problem 3
def enterNewPassword():
    while True:
        password = input("Enter a New Password: ")
        digit = False
        for x in password:
            if x.isdigit():
                digit = True
                break
        if (8 > len(password) or len(password) < 15) or not digit:
            if 8 > len(password) or len(password) > 15:
                print("the Password length must be between 8 and 15.")
            if not digit:
                print("Password Must contain one digit")
            else:
                return password
print(enterNewPassword(), "is a valid password")

print()


import random
num = 1
secretGuess = random.randint(0,50)
print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
print("guess", num,end="")
guess = int(input("? "))
while num != guess:
    if guess == secretGuess:
        print("You are right! I was thinking of", secretGuess)
        break
    elif num == 5:
        print("You ran out of guesses. I was thinking of the number", secretGuess)
        break
    else:
        num += 1
        if secretGuess > guess:
            print(guess, "is too low.")
            print("guess", num,end="")
            guess = int(input("? "))
        else:
            print(guess, "is too high")
            print("guess", num,end="")
            guess = int(input("? "))