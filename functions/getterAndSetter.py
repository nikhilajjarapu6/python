class A:
    def __init__(self,name,age,marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def marks(self):
        return self.__marks
    
    @name.setter
    def name(self,name):
        if len(name)<2:
            raise ValueError("name is too short")
        self.__name=name
    
    @age.setter
    def age(self,age):
        if(age<18):
            raise ValueError("age should be greater than 18")
        self.__age=age
    
    @marks.setter
    def marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            raise ValueError("enter correct marks")

    def display(self):
        print("student detailes")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Marks: {self.__marks}")
    
    def get_grades(self):
        match self.__marks:
            case m if m>=90:
                print("A grade")
            case m if m>=80:
                print("B grade")
            case m if m>=70:
                print("C grade")
            case m if m>=60:
                print("D grade")
            case _:
                print("failed")

a=A("alice",21,65)
a.display()
a.name="bob"
print(f"{a.name} of age is {a.age}")
a.display()
# print(a.__name)  #cannot access private variable
print(a._A__name)  
print(a.__dict__)
# print(A.__dict__)
print(a.marks)
a.get_grades()
a.marks="kjd"
a.get_grades()
