# Shailesh Yannam
# cs 100 2023S section 012
# HW 03,  February 12, 2023

# Excercise 1
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', "August", 'September', 'Cotober', 'November', 'December']
for x in months:
    if x.startswith("J"):
        print(x)

print()

# Excercise 2
for a in range(0,99):
    if a % 2 == 0 and a % 5 == 0:
        print(a)

print()

# Excercise 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for z in horton:
    if z in vowels:
        print(z)

print()

#Excercise 4
# Part 1
import math

factorial = math.factorial(100)

print(factorial)

print()

# Part 2
log = math.log2(1000000)

print(log)

print()

# Part 3
divisor = math.gcd(63,49)

print(divisor)


# Excercise 5
# Part a
import turtle

pen = turtle.Turtle()

# Equilateral Trangle
for x in range(3):
    pen.forward(100)
    pen.left(120)

# Square
pen.penup()
pen.forward(150)
pen.pendown()
for y in range(4):
    pen.forward(100)
    pen.left(90)

# Reqular Pentagon
pen.penup()
pen.forward(175)
pen.pendown()
for z in range(5):
    pen.forward(100)
    pen.left(72)

pen = turtle.Turtle()
pen.penup()
pen.forward(-250)
pen.pendown()
#Part b
# Circle Radius 50
pen.circle(50)

pen.penup()
pen.right(90)
pen.forward(50)
pen.left(90)
pen.pendown()

# Circle Raduis 100
pen.circle(100)

pen.penup()
pen.right(90)
pen.forward(50)
pen.left(90)
pen.pendown()

# Circle Radius 150
pen.circle(150)

pen.penup()
pen.right(90)
pen.forward(50)
pen.left(90)
pen.pendown()

# Circle Radius 200
pen.circle(200)

turtle.mainloop()
