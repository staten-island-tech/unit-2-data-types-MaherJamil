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
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" even_or_odd = input("Even or Odd?")
if even_or_odd == "1":
    print("Odd")
elif even_or_odd == "2":
    print("Even")
elif even_or_odd == "3":
    print("Odd")
elif even_or_odd == "4":
    print("Even")
elif even_or_odd == "5":
    print("Odd")
elif even_or_odd == "6":
    print("Even")
elif even_or_odd == "7":
    print("Odd")
elif even_or_odd == "8":
    print("Even")
elif even_or_odd == "9":
    print("Odd")
elif even_or_odd == "10":
    print("Even") """

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

Factor = input("Factor the number:")
if Factor == "4":
    print("1,2,4")
elif Factor == "6":
    print("1,2,3,6")
elif Factor == "10":
    print("1,2,5,10")
elif Factor == "16":
    print("1,2,,4,8,16")
elif Factor == "28":
    print("1,2,4,7,14,28")