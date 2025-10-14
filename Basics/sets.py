numbers={20,10,30,40,50,10,30,20}
print(numbers)

for n in numbers:
    print(n)
# for i in range(len(numbers)):
#     print(i,numbers[i])  index i not possible in sets

if 20 in numbers:
    print("yes")
if 200 not in numbers:
    print("no")

#to add one element
numbers.add(60)
print(numbers)

#to add multiple element at end
numbers.update({70,80})
print(numbers)

#adding iterable objects
numbers.update([90,100])
print(numbers)

li=list(numbers)
print(li,type(li))
li.append(110)
numbers=set(li)
print(numbers)

#joins
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

result = set1.union(set2)
print(result)

set3={1,2,4}
print(set2.union(set3))  #1234
print(set2.intersection(set3))  #12
print(set2.difference(set3)) #3
print(set3.difference(set2)) #3
print(set1.union(set2,set3))