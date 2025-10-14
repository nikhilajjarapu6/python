x=20;y=10;z=30

#normal if condition
if x>y:
    print("x is larger")
else:
    print("y is larger")

if x>y : print("x is larger")
#short hand technique
print("x is larger") if x>y else print("y is larger")

#terinary operator
print("x is larger") if x>y else print("=") if x==y else print("y is larger")

#elif
if x>y:
    print("x is greater")
elif x==y:
    print("x and y are both equal")
else :
    print("y is greater")



# isfail=True
# while isfail:
#     grade=input("enter you grade")
#     if grade=='A':
#         print("excellent")
#     elif grade=='B':
#         print("very good")
#     elif grade=='C':
#         print("good")
#     elif grade=='D':
#         print("avg")
#     else :
#         print("fail")
#         isfail=False
      

a = 10
b = 25
c = 17

if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

#example for nested
if b>a:
    if b>c:
        print("b is largest")
    elif c>a:
        print("c is greater")
    else:
        print("a is greater")
#with ternary operator
largest = a if (a > b and a > c) else (b if b > c else c)
print("Largest is:", largest)
print(f"largest = {largest}")

#AND
if c>a and b>c:
    print("true both numbers are greater than a")

#or
if a>b or b>c:
    print("true one of the condition was true")

#NOT
if not a>b:
    print("a is not greater than b")

#pass
if a>b:
    pass  #it does nothing

#break
for x in range(1,5):  #123
    if x==4:
        break    #breaks the loop and exit immediatly
    print(x)
print("..................")

#continue
for x in range(1,5):
    if x==2:
        continue
    print(x)
print("..................")

#pass
for x in range(5):
    if x==2:
        pass #does nothing, future we can write logic
    print(x)
print("..................")
#loop with else
for x in range(5):
    if x==5:
        print("break happend")
        break
else:
    print("no breaks")     #indicates no breaks happend in loop

# day=int(input("enter day"))
day=1
match day:
    case 1:
         print("sunday")
    case 2:
        print("monday")
    case 3:
         print("tuesday")
    case 4:
         print("wednesday")
    case 5:
         print("thursday")
    case 6:
         print("friday")
    case 7:
        print("saturday")
    case _:
        print("default value")

match day:
    case 2 | 3 | 4 | 5 | 6 :
        print("week day")
    case 1|7:
        print("weekend")
    case  _:
        print("default value")
