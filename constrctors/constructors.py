class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        print("from class constructor............")
    
    @classmethod
    def from_data(cls,data:str):
        name,breed=data.split("-")
        print("from class method constructor....................")
        return cls(name,breed)     #it will call class constructor
    @classmethod
    def from_dict(cls,data:dict):
        name,breed=data["name"],data["breed"]
        print("from class method constructor....................")
        return cls(name,breed)
obj=Dog("lucy","husky")
print(obj.name,obj.breed)
obj2=Dog.from_data("tommy-Retriever")
print(obj2.name,obj2.breed)
dog=Dog.from_dict({"name":"john","breed":"Retriever"})
print(dog.name,dog.breed)
        
