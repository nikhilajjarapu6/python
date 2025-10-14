class A:
    def __init__(self,name="none",age=0):
        self.name=name
        self.age=age
a=A("john cena",23)
print(a.name,a.age)
b=A("faf")
print(b.name,b.age)
c=A()
print(c.name,c.age)
# d=A(23)  first param as name so 23 will become name
d=A(age=23)
print(d.name,d.age)
        