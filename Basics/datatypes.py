#integers/numbers
a=10 #a=int(10)
print(f"number {a} data type {type(a)}")

f=10.9 #f=float(10.9)
print(f"number {f} data type {type(f)}")

c=1j
print(f"number {c} data type {type(c)}")

x = 1    # int
y = 2.2  # float
z = 1j   # complex
a=float(x);b=int(y)
# c=float(z)  we cannot convert complext to any other format
print(a,b,c)
print(type(a),type(b))

#complex number separating real and imaginary
p=3+5j
print(p.real,p.imag)

#tyr conversion of string to float
num="23333.42"
print(float(num),type(float(num)))


""" Boolean data type"""
a, b = True, False
print("AND:", a and b)  # False
print("OR:", a or b)    # True
print("NOT:", not a)    # False

# String data type 
name="john wick"
gender="male"
print(name,"was 10 year old and he was",gender)
lorem="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna 'aliqua'."""
print(lorem)

print(*name,sep=",",end="")
print("cena")

print(" ".join(name))
print("new line")

print("length of",name,len(name))
print(f"length of {name} is {len(name)}")

txt=" java is best in the world "
if("java" in txt):
    print(True)
else:
    print(f"{False} java is not presented in given text ")

if "python"  not in txt:
    print(True)

#slicing strings
print(name[0:len(name)])
print(name[1:4])
print(name[-5:-1])
print(name[1:])
print(name[-len(name):])

#modifi strings
print("word",name,"converting into uppper case",name.upper())
print("word",name,"converting into lower case",name.lower())
# print("finding index of substring",name.index("zj"))
print("removing trail spaces of string",name.strip("j"),id(name.strip(" ")))
print(name,id(name))
print("replacing string",name.replace("j","J"))
print("replacing string",name.replace(""," "),id(name.replace(" ","")))

string="hello,world"
print(string.split(","),type(string.split(",")))  #returns list of substrings
print(string.count("l"))




