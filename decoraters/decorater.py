def my_decorater(func):
    def wrapper(*args,**kwargs):
        print("step 3: inner function started executeing..........")
        print(f"step 4: mydecorater: args:{args}, kwargs:{kwargs}")
        result=func(*args,**kwargs)
        # print(result)
        print("step 5:inner function completed executing...........")
        return result
    return wrapper

def change_case(func):
    print("wrapper function ......")
    def wrapper(*args,**kwargs):
        print("step 1: from wrapper function.....")
        print(f"step 2: changecase:args:{args}, kwargs:{kwargs}")
        result=func(*args,**kwargs).upper()
        print("step 6:wrapper function exit.....")
        return result
    return wrapper

@change_case
@my_decorater
def greet(*names):
    if len(names)==1:
        return f"hello {names[0]}"
    else:
         return f"hello {names[0]} and {names[1]}"

@change_case  
def uppercase(msg):
    return f"convertig {msg} into uppercase"   #for decorater modify the original function it must return something 
   

if __name__=="__main__":
    # print("basic decorater example")
    # result=greet("max")
    # print(result)
    print("=="*50)
    print(greet("shawn","haris"))
    # print(uppercase("mike"))
