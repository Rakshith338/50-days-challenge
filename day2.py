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
