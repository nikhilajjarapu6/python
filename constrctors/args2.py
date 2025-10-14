class A:
    def __init__(self, *args, **kwargs):
        # defaults
        self.name = "unknown"
        self.age = 0

        # handle positional args
        if len(args) == 2:
            self.name, self.age = args
        elif len(args) == 1:
            if isinstance(args[0], str):
                self.name = args[0]
            elif isinstance(args[0], int):
                self.age = args[0]
        
        # handle keyword args
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "age" in kwargs:
            self.age = kwargs["age"]
a=A("John", 25)
print(a.name,a.age)
b=A("Rock")
print(b.name,b.age)
c=A(30)
print(c.name,c.age)
d=A()
print(d.name,d.age)
e=A(name="Cena", age=40)
print(e.name,e.age)


class B:
    def __init__(self,*args,**kwargs):
        print(type(args),type(kwargs),".....................")  #tuple lsit and dict
        self.name=args[0]
        self.age=args[1]
        if "last" in kwargs:
            self.last=kwargs["last"]
        if "sex" in kwargs:
            self.sex=kwargs["sex"]
    
a=B("john",21)
print(a.age,a.name)
b=B("john",21)
print(b.name,b.age)
c=B("john",21,last="wick",sex="male")   #sending noth tuples and dict values
print(c.name,c.age,c.last,c.sex)
