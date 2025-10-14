i=1
while i<=5:
    print(i)
    i+=1#
print(i)
# while i<10:
#     if i==8:
#         continue
#     print(i)
#     i+=1
# print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

adj = ["red", "big", "tasty"]

for x in adj:
  print("from inner loop..............")
  for y in fruits:
    print(x, y)


for i,x in enumerate(adj):
  print("executing outer index :",i)
  for j,y in enumerate(fruits):
    print("executing inner index :",j)
    print(x, y)

for i in range(5):
   print("executing outer index :",i)
   for j in range(5):
       print("executing inner index :",j)

name="john wick"
for x in name:
   print(x)
