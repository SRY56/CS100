# Shailesh Yannam
# cs 100 2023S section 012
# HW 02, February 2, 2023

# Excercise #1
# Part A
a = 3
b = 4
c = 5

# Part B
if a < b:
    print("Ok")

# Part C
if c < b:
    print("Ok")

# Part D
if a + b == c:
    print("Ok")

# Part E
if (a**2) + (b**2) == (c**2):
    print("Ok")

print()

# Excercise #2
# Part B2
if a < b:
    print("Ok")
else:
    print("Not OK")

# Part C2
if c < b:
    print("Ok")
else:
    print("Not Okay")

# Part D2
if a + b == c:
    print("Ok")
else:
    print("Not Okay")

# Part E2
if (a**2) + (b**2) == (c**2):
    print("Ok")
else:
    print("Not Ok")

print()

# Excercise #3
grades =  ['A', 'C', 'F', 'D', 'A', 'F', 'B', 'C', 'A', 'B']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)

print()

# Excercise #4
# Part 4A
dog_breeds = ['Collie', 'Sheepdog', 'Chow', 'Chihuahua']

print(dog_breeds)

# Part 4B
herding_dogs = dog_breeds[0:2]

print(herding_dogs)

# Part 4C
tiny_dogs = dog_breeds[-1:] 

print(tiny_dogs)

# Part 4D
if ("Persian" in dog_breeds):
    print(True)
else:
    print(False)