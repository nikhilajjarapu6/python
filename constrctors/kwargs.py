class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def multi_kwargs(cls,*args,**kwargs):
        name=kwargs["name"]
        age=kwargs["age"]
        print(args)
        print(kwargs)
        return cls(name,age)
    def my_function(self,**kid):
        print("His last name is " + kid["lname"])
    def country(self,country = "Norway"):     #default value
        print("I am from " + country)




obj=A(name="american",age=21)
print(obj.name,obj.age)
obj2=A.multi_kwargs(22,name="american",age=21,sex="male")
print(obj2.name,obj2.age)
obj2.my_function(fname = "Tobias", lname = "Refsnes")
obj2.country("india")
obj2.country("eng")
obj2.country()