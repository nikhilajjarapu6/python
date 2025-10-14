
num1=10
#reassingment of varibale creates new object instead of in same object
print(f"address of{num1} is id: {id(num1)}")
num1=30
print(f"address of{num1} is id: {id(num1)}")

s="python"
print(s+" is awsome and address of string "+str(id(s)))
s="java"
print(s+" is awsome and address of string "+str(id(s)))