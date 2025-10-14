numbers=(10,30,20,50,40)
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[::2]) #alternative
print(numbers[:4]) 
print(numbers[0:])
print(numbers[-4:-1])  #always left side inculded and right side excluded
print(numbers[0])  #accessing tuple element

#numbers[4]=60 #type error,tuple is unchangeble

#converting
li=list(numbers)
print(li)
print(type(li))  #now we can modifiy the list
li.append(60)    #append value 
li[len(li):len(li)]=[70,80,81,90]
numbers=tuple(li) #re assign into exisitng tuple
print(numbers,type(numbers))

li=list(numbers)
li.remove(90)
numbers=tuple(li)
print(numbers)

li=list(numbers)
# if 81 in li:
#     print(li.index(81))
# li[8]=90
li=[num if num!=81 else 90 for num in li]
numbers=tuple(li)
print(numbers)

# li=list(numbers)
# [num if num!=81 else 90 for num in numbers]

fruits = ("apple", "banana", "cherry","berry","dragon")
(green, yellow, red,white,black) = fruits  
print(green)
print(black)

(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)   #remaining elements added to the red literal

(green,*yellow,red)=fruits
print(green)
print(yellow) #total 5 elements *takes three elements two elements for two literals
print(red)
# (green,*yellow,red)=fruits  cannot add two astricks * in same unpacking

print(numbers.count(10))