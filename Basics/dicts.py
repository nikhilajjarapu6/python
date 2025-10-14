dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2010,
  "colors": ["red", "white", "blue"]
}
print(dic["year"])
print(len(dic))
print(type(dic))
print(dic)
print(dic.get("model"))  #return value for key if its present or return none
print("items of dict",dic.items())
print("values of dict",dic.values())
print("keys of dict",dic.keys())
print("length of items",len(dic.items()))
print("type of dic items ",type(dic.items()))
print(dic.get("colors"))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict["sex"]="male"
print(thisdict)
thisdict.update({"last":"wick"})
print(thisdict)
if "name" in thisdict:
     print("yes")


# thisdict.pop("last")  #removes specified key 
# thisdict.popitem() #removes last inserted key
del thisdict["last"]  #deletes specified key and value
# del thisdict  deletes whole dict
# thisdict.clear() clear items in dict

for key in dic:
     print(dic[key])

for key in dic.keys():
     print(dic[key],end=" ")
print()
for value in dic.values():
     print(value)

for k,v in dic.items():
     print(f"{k} = {v}")

print(dic["colors"])

nested_dict = {
    "fruit": {
        "apple": {"color": "red"},
        "banana": {"color": "yellow"}
    }
}
print(nested_dict)
print("banana color =",nested_dict.get("fruit").get("banana").get("color"))  #nested accessing
print("banana color =",nested_dict.get("fruit",{}).get("banan",{}).get("color","no color"))  #{} empty set makes sures return dealut value when key is not presented
print("apple color =",nested_dict["fruit"]["apple"]["color"])

print("..........................")
for k,v in nested_dict.items():
     print("key=",k)
     for i,j in v.items():
          print("key=",i)
          for n,m in j.items():
               print("key=",n,"value=",m)

family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}
print(family["child2"]["year"])