g = 10  # global variable

class Demo:
    x = 10  # class-level variable

    @staticmethod
    def inner():
        # This 'x' is a local variable to the inner() static method.
        # It does not affect the class variable Demo.x
        x = 20
        print(x, "local variable inside static method Demo.inner()")

    @staticmethod
    def mod():
        # Using 'global g' to modify the global variable 'g'
        global g
        g = 30
        print(g, "modified global value inside static method Demo.mod()")
        print(Demo.x,".............................")
        Demo.x=0

    @classmethod
    def classVariable(cls):
        # 'cls' refers to the class itself (Demo in this case).
        # cls.x to access and modify the class variable Demo.x
        cls.x *= 10
        print(f"Class variable Demo.x modified to {cls.x} by classmethod Demo.classVariable()")

Demo.inner()

print(Demo.x, "class variable (unaffected by inner's local x)")

print(g, "global level variable before modification by Demo.mod()")
Demo.mod() # This will modify the global 'g'
print(g, "global level variable after modification by Demo.mod()")

Demo.classVariable() # This will modify Demo.x
print(Demo.x, "class variable after modification by Demo.classVariable()")

print(g, "global variable (final value)")
print(Demo.x, "class variable (final value)")