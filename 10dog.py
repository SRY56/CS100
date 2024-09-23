# Shailesh Yannam
# CS 100 2023S Section 012
# HW 10, April 21, 2023

# Exercise 01
class Dog: 
# Exercise 05
    species = "canis familiaris"
    def __init__(info, name, breed):
        info.name = name
        info.breed = breed
# Exercise 02
        info.tricks = []
# Exercise 03
    def teach(info, trick):
        info.tricks.append(trick)
        print(info.name + ' knows ' + trick + '.')
# Exercise 04
    def knows(info,trick):
        if trick in info.tricks:
            print(info.name + " does know " + trick + ".")
            return True
        else:
            print(info.name + " does not know " + trick + ".")
            return False
# Tests for all exercises

import dog
nick = dog.Dog('Nick', 'poodle')
print(nick.name)
print(nick.breed)
print(nick.tricks)
print(nick.teach("frisbee"))
print(nick.knows("frisbee"))
print(nick.knows("arithmetic"))
print(nick.species)
print(dog.Dog.species)