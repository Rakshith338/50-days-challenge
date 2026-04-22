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
else:
        print ("invalid")
        
"""
output:enter the first number: 25
enter the second number: 26
enter the third number: 28
28 is largest number
"""

