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
"""

#Task#3: Largest of 3 numbers
