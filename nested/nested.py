class A:
   def __init__(self):
      pass
   
   def outer():
      print("outer function")
      def inner():
         print("inner function")
      inner()
   def outer_function(self,x):
    # This is the outer function
    print(f"Outer function received: {x}")

    def inner_function(y):
        # This is the inner (nested) function
        # It has access to 'x' from the outer function's scope
        print(f"Inner function received: {y}")
        return x + y

    # The outer function can call the inner function
    result = inner_function(5)
    print(f"Result from inner function: {result}")
    return result

a=A()
a.outer()
a.outer_function(10)
         
        