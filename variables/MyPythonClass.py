print("1. Before class definition")

class MyPythonClass:
    print("    2. Inside class definition - this executes IMMEDIATELY when class is defined")
    CLASS_VARIABLE = "I am a class attribute (like Java static)" # Defined and initialized here
    print(f"    3. CLASS_VARIABLE initialized to: {CLASS_VARIABLE}")

    def __init__(self, instance_value):
        # This method only executes when an INSTANCE is created
        self.instance_variable = instance_value
        print(f"        5. __init__ executed. Instance variable set to: {self.instance_variable}")

    def a_method(self):
        print("        Method 'a_method' called on an instance.")

print("4. After class definition - class object 'MyPythonClass' now exists")

# Instance creation
obj1 = MyPythonClass("first instance data")
obj2 = MyPythonClass("second instance data")

print(f"6. obj1.CLASS_VARIABLE: {obj1.CLASS_VARIABLE}")
print(f"7. obj2.CLASS_VARIABLE: {obj2.CLASS_VARIABLE}")

# You can also access class variables directly from the class object
print(f"8. MyPythonClass.CLASS_VARIABLE: {MyPythonClass.CLASS_VARIABLE}")