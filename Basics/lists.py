numbers=[30,10,20,40]
digits=[70,100,90,80]

# numbers.extend(digits)
print(numbers[2])
print(numbers[-1])
print(numbers[0:len(numbers)])
print(numbers[1:])
print(numbers.index(20)) #returns index
numbers.sort()    #sorts list
numbers.append(50)
numbers.append(60)  #10,20,30,40,50,60
print("pop operation",numbers.pop(len(numbers)-1))
print(numbers.count(10))
numbers.remove(50)
print(numbers)
if 50 in numbers:
    print(True)
else:
    print(False)

#inserting numbers
numbers.append(50)
numbers.insert(len(numbers),60)
print(numbers,id(numbers))

#extending lists
numbers.extend(digits)
print(numbers,id(numbers))


fruits=["apple", "banana", "cherry"]
if "apple" in fruits:
    print("yes")
#accessing
print(fruits[0])
#printing along with index
for index,f in enumerate(fruits):
    print("index",index,":",f)
for index,f in enumerate(fruits,start=1): #to start desired number
    print("index",index,":",f)

#adding elements to the existing list
fruits[1]="berry" #replaces item at specified index
fruits[1:1]=["banana","grape"]  #start=1 and end=1 so it will add items at index without replacing
print(fruits)
# fruits.append(("orange", "kiwi", "mango"))
# fruits.extend(["orange", "kiwi", "mango"])
# fruits[len(fruits):3]=["orange", "kiwi", "mango"]
fruits=fruits+["orange", "kiwi", "mango"]
fruits.insert(3,"berry")
print(fruits)

#remove itmes from list
fruits.remove("berry") #removes item from list
# fruits.pop(1) #removes specified index item from list 
del fruits[2]   #deletes sepcified index item from list 
# del fruits
# print(fruits)  #name error because fruits are deleted
# fruits.clear()   #clears whole list 
print(fruits)
list = fruits.copy()  #copies whole list
print(list) 

#loops
for fruit in fruits:
    print(fruit)

for i in range(len(list)):
    print(list[i]+" "+str(i))

index=0
while index<len(list):
    print(list[index],"index number is",index)
    index=index+1

#comprehension
greater = [num for num in numbers if num>=50]
print(greater)

mul=[num*10 for num in numbers] #transforming
print(mul)

sliced=[fruit for fruit in fruits if fruit[0:1]=='a' or fruit[0:1]=='b']
print(sliced)

upper=[fruit.upper() for fruit in fruits]
print(upper)


#sortig
print(sorted(numbers),id(sorted(numbers))) #sort method to return new sorted list
numbers.sort()         #sort method to sort original list
print(numbers,id(numbers))

print(sorted(numbers,reverse=True))  #sort the numbers in reverse order
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits) 
fruits.sort(key=len)
print(fruits)

def length(string):
    return len(string)

fruits.sort(key=length)
print(fruits)

