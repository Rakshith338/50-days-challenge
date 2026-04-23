#task1 : print number using loop

for x in range(1,11):
    print (x)


for x in range(1,11):
    if x % 2 == 0:
        print(x)

# output in horizontal line
#  Use end=" " ,sep="-",

# new line : print() , print("\n")   # newline

for x in range(1,11):
    print (x, end=" ")

print()                       # 👈 moves to next line

for y in range(1,11):
    if y % 2 == 0:
        print(y, end=" ")




#taks2: sum of list

x = [10, 20, 30, 40]
total = sum(x)
print()
print (total)

#using loop with function call

def fun(total):
    print(total)
    
x = [10, 20, 30, 40]  # index as i

total = 0
for i in x:
    total = total + i
    print (total)

fun(total)

"""
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 
100
10
30
60
100
100
"""

#task3 : largest number in list

def fun(num):
    print (num)

number = [20, 25, 30]
fun(number)

num = number[0]
for i in number:
    if i > num:
        num = i

print(f"Largest: {num}")

"""
[20, 25, 30]
Largest: 30
"""


