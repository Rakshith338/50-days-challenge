#variables

a = 10          #integer variable
name = "rakshi" #string variable
b = 5.5         #floating variable
print(a,b,name) #built in function

#input to variables

a = input("enter first number: ") #input as string
b = input ("enter second number: ")
print (a,b)

a = int(a)
b = int(b)    
c = a +b      # add operator
print (c)

#build my simple calculator
#using input & operation
#using formating strng output

x = input("enter the x value:")
y = input("enter the y value:")
x = int(x)
y = int(y)

print (f"additon: {x+y}")
print (f"substraction:{x-y}")
print (f"multiplication:{x*y}")
print (f"division: {x/y}")
print (f"modulus: {x%y}")

#start if condition
#odd and even numbers

x = 5

if x % 2 == 0:
    print ("x is even number")
elif x % 2 != 0:
    print ("x is odd number")

#build calculator
#using input,variable, operators & if conditions

a = int(input("enter the first value: "))
b = int(input("enter the second value: "))

print("selection:")
print("1.addition:")
print("2.substraction:")
print("3.multiply:")
print("4.division:")

choice = input("select choice(1/2/3/4):")

if choice == "1":
    print(f"Result:{a+b}")

elif choice == "2":
    print(f"Result:{a-b}")

elif choice == "3":
    print(f"Result:{a*b}")

elif choice == "4":
    print(f"Result:{a/b}")

else:
    print ("invalid choice")





