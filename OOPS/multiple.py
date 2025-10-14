class A:
    def run(self):
        print("from class A")
class B(A):
    def method1(self):
        print("from class B")
    def run(self):
        print("B class overrides A class run method")
        super().run()   #calls next mro order class method
class C(A):
    def method2(self):
        print("from class C")
    def run(self):
        print("C class overrides A class run method")
class D(B,C):
    def show(self):
        print("from D class")
        super().run() #calls next mro order is B(run method)
    def run(self):
        print(f"from D class run method")

d=D()
d.run()  #calls B run method
d.show()
print(D.__mro__) #methods will be executed on method resoultion order (MRO)




