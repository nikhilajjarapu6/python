class Person:
    def __init__(self,name,age):
        self.__name=name   #private values will be saved in memory like _Classname__var = _Person__name
        self._age=age      #proteced values will be saved in memory like _var = _age

    @property
    def name(self):
        return f"person name:{self.__name}"
    
    @property
    def age(self):
        return f"person age:{self._age}"
    
    @name.setter
    def name(self,name):
        if name is not None:
            self.__name=name
        else:
            print("name should not be none")
    @age.setter
    def age(self,age):
        if age>0:
            self._age=age
        else:
            print("age should be greater than zero")
        
    def __str__(self):
        return f"{self.__name} age was {self._age}"
        
if __name__=="__main__":
    person=Person("mike",27)
    print(person)
    print(person._Person__name) #can access private but not encouraged
    print(person.name)
    print(person._age)  #can access protected but not encouraged
    print(person.age)
    person.name="shawn"
    print(person)


