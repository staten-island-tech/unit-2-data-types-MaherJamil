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
""" function = int(input("Enter a number: "))
print(f"{function}, 1")
if function%2 == 0:
    print("2")
if function%3 == 0:
    print("3")
if function%4 == 0:
    print("4")
if function%5 == 0:
    print("5")
if function%6 == 0:
    print("6")
if function%7 == 0:
    print("7")
if function%8 == 0:
    print("8")
if function%9 == 0:
    print("9")
if function%10 == 0:
    print("10")
if function%11 == 0:
    print("11")
if function%12 == 0:
    print("12")
if function%13 == 0:
    print("13")
if function%14 == 0:
    print("14")
if function%15 == 0:
    print("15") """

#Challenge 4
number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

