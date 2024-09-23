# Shailesh Yannam
# cs 100 2023S section 012
# HW 09, April 21, 2023

#Excercise 1:
def safeOpen(filename):
    try:
        inFile = open(filename)
    except(FileNotFoundError):
        return None

inputfile = safeOpen("ghost.ext")
print(inputfile)

print()

#Ecercise 2:
def safeFloat(x):
    try:
        floats = float(x)
        return floats
    except(ValueError):
        return 0.0

trial = safeFloat("abc")
print(trial)

print()

#Excercise 3
def averageSpeed():
    attempts = 1
    while (attempts <= 2):
        try:
            fileName = open(input("Enter file name: "), "r")
            spaces = fileName.readlines()
            sum = 0.0
            count = 0
            for space in spaces:
                x = space.split(' ')
                for y in x:
                    try:
                        z = safeFloat(y)
                        if z>2:
                            sum = sum + safeFloat(y)
                            count = count + 1
                    except ValueError:
                        pass
            print("The Average speed is {} miles per hour".format(round(sum/count,2)))
            break
        except FileNotFoundError:
            if attempts == 1:
                print("FIle not found. Please try again")
            else:
                print("File not found. Yet another human error. Goodbye")
        attempts = attempts + 1
averageSpeed()