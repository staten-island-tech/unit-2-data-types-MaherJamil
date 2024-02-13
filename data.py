""" import math
from math import * """
""" #Data Types
#Numbers 1,2,3
def add(x,y):
    print(x + y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#undefined/null

#booLeans
tenure = True
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("they are not tenured") """

""" x=3
y=float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
 """
""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Challenge 1
""" even_or_odd = int(input("Enter a number: "))
if (even_or_odd % 2) == 0:
   print("Even")
else:
   print("Odd") """

#Challenge 2
""" x= "0%,15%,20%,25%"
print(f"{x}")
Tip = input("How much would you liek to tip?")
if Tip == "0%":
    print("The service was bad")
elif Tip == "15%":
    print("The service was okay")
elif Tip == "20%":
    print("The service was good")
elif Tip == "25%":
    print("The service was great") """
 
#Challenge 3
"""number = int(input("Enter a number:"))
for i in range(1, number + 1):
    if number % i == 0:
        print(i) """
 
#Challenge 4 
"""number = int(input("Enter a number:"))
number2 = int(input("Enter a second number:"))
gcf = gcd(number, number2)
print(f"The GCF of {number} and {number2} is {gcf}") """

#Calculator
"""Bill = float(input("Enter amount: "))
x ="0%, 15%, 20%, 25%"
print(x)
Tip = input("Select Tip:")
if Tip == "0%":
    print(Bill)
elif Tip == "15%":
    Bill = Bill*1.15
    print(f"Amount: {Bill}")
elif Tip == "20%":
    Bill = Bill*1.2
    print(f"Amount: {Bill}")
elif Tip == "25%":
    Bill = Bill*1.25
    print(f"Amount: {Bill}") """

#Challenge 4.5
x=4
y=5
def check_if_4(x,y):
    if(x == 4 and y == 4):
        print("both are 4")
    else:
        print("1 or 0 are 4")
#check_if_4(x,y)
        
print(factors[-1])

