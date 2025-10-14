print("welcome to python variables")

#variable declerations
x=10;y=20;z='c'

# declaring multiple variable
a,b,c=10,20,30
print(a,b,c)

#concatinating
print("sum is",a+b+c)
print("sum of",a,b,c,"is",a+b+c)
print("sum of "+str(a)+","+str(b)+","+str(c)+" is",(a+b+c))
print(f"sum of {a},{b},{c} is {a+b+c}")
# string declerations
first_name="john"
last_name="wick"

# concating strings and variables
print("two variables are",x,y,first_name)
print("sum of two numbers with name",str(x),str(y),first_name)
print(f"enter full name : {first_name} {last_name}")
print("sum of number",x,"+",y,"is =",(x+y))
print(f"sum of number {x} + {y} is {(x+y)}") 

#string concat with number
print("first name "+first_name+" and number is "+str(x))

# data type of variables
print(f"data type of {type(x)}")
print(f"data type of {type(first_name)}")
print(f"data type of {type(z)}")

# reinitialization of variabels
last_name="paul"
print(f"name was changed from wick to {last_name}")



# declaring constant values
CONSTANT=3.14
print("constant value",CONSTANT)

# delete keyword
d = 100
print("new variable value",d)
print("deleting d value...........")
del d
# print(d,"sucessfully deleted") #fail due to deletion of value d 


#global varibales
global word,code
word = "python"  # global variable
code="hello"

def myfunc():
    word = "java"   # local variable with same name
    print(word+" is awsome")     # prints local "java"
    # global word is shadowed and can't be accessed directly
    print(globals()['word'])  # prints global variable "python"

myfunc()
print(word+" is awsome")  # prints global "python"
