class A:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print("from parameterized constructor")
    @classmethod
    def from_data(cls,data:tuple):                   #ostly used to parse different data types into construcotr 
        name,age,sex=data[0],data[1],data[2]        
        return cls(name,age,sex)
a=A("john wick",23,"male")
print(a.name,a.age)
b=A.from_data(("rock",25,"male"))   #tuple data
print(b.name,b.age,b.sex)