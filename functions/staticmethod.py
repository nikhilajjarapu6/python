import math


class A:
    num=10
    
    def __init__(self,value):
        self.value=value
    
    def add(self,number):
        self.value+=number
    
    @staticmethod
    def pi():
        print("from static method")
        return math.pi
    
    @staticmethod
    def is_positive(number):
        return number>0
a=A(20)
a.add(30)
print("added numbers value",a.value)
a.add(30)
print("added numbers value",a.value)
print(A.pi())
print(f"20 is positive number? {A.is_positive(20)}")