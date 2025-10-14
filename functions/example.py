def myfunction():
    print("hello from my function")

myfunction()

def my_function(fname, lname):
  print(fname + " " + lname)

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Refsnes")
my_function("Emil", "Tobias", "Linus")
