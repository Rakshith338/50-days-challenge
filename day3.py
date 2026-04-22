#Task 1: even or odd checker

a = int(input("enter the number: ")) #Take input

if a % 2 == 0:           # print whether 
        print("even")
else:
    print ("odd")

#output
"""
enter the number: 6
even
"""

#Task#2 : simple calculator


a = int(input("enter the first number: ")) #Take input
b = int(input("enter the second number: ")) #Take input

enter_operation = input("enter operation (+,-,*,/):")


if enter_operation == "+":
    print(f"output:{a + b}")
    
elif enter_operation == "-":
    print(f"output:{a - b}")

elif enter_operation == "*":
    print(f"output:{a * b}")

elif enter_operation == "/":
    print(f"output:{a / b}")

else:
    print("invalid operation")

"""
enter the number: 5
odd
enter the first number: 5
enter the second number: 5
enter operation (+,-,*,/):8

output:10

enter the number: 8
even
enter the first number: 6
enter the second number: 6
enter operation (+,-,*,/):8
invalid operation
enter the first number: 5
enter the second number: 5
enter operation (+,-,*,/):*
output:25
"""

#Task#3: Largest of 3 numbers
#20, 25, 26

a = int(input("enter the first number: ")) #Take input
b = int(input("enter the second number: ")) #Take input
c = int(input("enter the third number: ")) #Take input

if a > b and a > c:
        print (f"{a} is largest number")
elif b > c and b > a:
        print (f"{b} is largest number")
elif c > a and c > b:
        print (f"{c} is largest number")
else:                                     #Note:no coditions provided for else
        print ("invalid")
        
"""
output:enter the first number: 25
enter the second number: 26
enter the third number: 28
28 is largest number
"""

#Mini project(important)
# Project name: Number Guessing name"

"""
What is a module?

A module = a file that contains Python code (functions, variables, etc.)

Examples:

random → random numbers
math → mathematical functions
datetime → date & time
"""

import random

print(random.randint(1, 6))   # like rolling a dice 🎲import random


import random                          # random number by computer (import is used to bring code from another module (file/library) into your program.)
number = random.randint(1,10)            # list of 1 to 10
guess = int(input("enter your guess(1-10): "))

print("computer number:", number)

if guess > number:
        print("too high")

elif guess < number:
        print ("too low")

elif guess == number:
        print ("correct")

else:
        print ("invalid")

"""
enter your guess(1-10): 8
computer number: 5
too high
"""

import random                          # random number by computer (import is used to bring code from another module (file/library) into your program.)
number = random.randint(1,10)            # list of 1 to 10
guess1 = int(input("enter your guess(1-10): "))

if guess1 > number:
        print("too high")

elif guess1 < number:
        print ("too low")

elif guess1 == number:
        print ("correct")

guess2 = int(input("enter your guess(1-10): "))

if guess2 > number:
        print("too high")

elif guess2 < number:
        print ("too low")

elif guess2 == number:
        print ("correct")

guess3 = int(input("enter your guess(1-10): "))
print("computer number:", number)


if guess3 > number:
        print("too high")

elif guess3 < number:
        print ("too low")

elif guess3 == number:
        print ("correct")

elif guess1 and guess2 and guess3 != number:
        print ("game over")


import random                          # random number by computer (import is used to bring code from another module (file/library) into your program.)
number = random.randint(1,10)            # list of 1 to 10
guess1 = int(input("enter your guess(1-10): "))
guess2 = int(input("enter your guess(1-10): "))
guess3 = int(input("enter your guess(1-10): "))
print("computer number:", number)

if (guess1) and (guess2) and (guess3 == number):
        print("correct")

elif (guess1) and (guess2) and (guess3 != number):
        print ("game over")

import random                          # random number by computer (import is used to bring code from another module (file/library) into your program.)
number = random.randint(1,10)            # list of 1 to 10
guess1 = int(input("enter your guess(1-10): "))
guess2 = int(input("enter your guess(1-10): "))
guess3 = int(input("enter your guess(1-10): "))
print("computer number:", number)

if guess1 == number or guess2 == number or guess3 == number:
        print("correct")

else:
        print ("game over(3 attempt used")


#it is nice i will try on day4.py

import random

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("Enter your guess (1-10): "))

    if guess == number:
        print("Correct!")
        break
else:
    print("Game Over! Number was:", number)




