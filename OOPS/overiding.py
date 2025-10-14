class Animal:
    def __init__(self,name):
        self.name=name
        print(id(self))
        print(f"{self.name} from super class")
    
    def speak(self):
        print(f"{self.name} making sound")
    
    def run(self):
        print("from superclass method")
    
    def info(self,name):
        print(f"executing from info method of parent {name}")

class Dog(Animal):
    def __init__(self,name,breed,color):
        print(id(self))
        super().__init__(name)   #calling parent constructor
        self.breed=breed
        self.color=color
    
    #method overiding. dog speak method overides animal speak method
    def speak(self):
        print(f"{self.name} is making sound")
        print(f"{self.breed} barking")
    
    def run(self):
        print("from subclass method")

    def info(self,name,last="child"):
        super().info(name)
        print(f"executing from info method of parent {name},{last}")

animal=Animal("Tiger")
animal.speak()
animal.run()


dog=Dog("lion","Husky","white")
dog.speak()
dog.run()
print(dog,animal)
dog.info("Animal")


        