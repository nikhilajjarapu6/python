class Dog:
    species = "Canis familiaris" # Class attribute

    def __init__(self, name, breed):
        self.name = name   # Instance attribute
        self.breed = breed # Instance attribute
        self.is_hungry = True # Instance attribute

    def bark(self): # Instance method
        # 'self' refers to the specific dog object that barks
        print(f"{self.name} barks: Woof!")
    def eat(self): # Instance method
        if self.is_hungry:
            print(f"{self.name} is eating...")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")

my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Beagle")

my_dog.bark() # Buddy barks
your_dog.bark() # Lucy barks
my_dog.eat() # Buddy eats
my_dog.eat() # Buddy is not hungry
your_dog.eat() # Lucy eats (she's hungry)