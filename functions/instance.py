class A:
    def __init__(self,value):
        self.value=value

    def instance(self,msg):
        print("instance varibale",self.value)
        print(f"{msg} was best language")
        self.value=msg
        print("modifed instance variable",self.value)
        print(type(self),"...................")

a=A(20)
print(a.value)        
a.instance("python")

b=A(30)
b.instance("java")
print(a,b,"both will have different address")
b=a
print(b.value)
print(a,b,"both referes same object")