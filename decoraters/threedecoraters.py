def decorater1(func):
    def wrapper(*args,**kwargs):
        print("step 1: entering decorator1.wrapper (outermost)")
        result=func(*args,**kwargs)
        print("step 7: exiting decorater1.wrapper (outermost)")
        result=result+100
        return result
    return wrapper

def decorater2(func):
    def wrapper(*args,**kwargs):
        print("step 2: entering decorater2.wrapper (middile layer)")
        result=func(*args,**kwargs)
        print("step 6: exiting decorater2.wrapper (middile layer)")
        result=result*10
        return result
    return wrapper

def decorater3(func):
    def wrapper(*args,**kwargs):
        print("step 3: entering decorater3.wrapper (inner layer)")
        result=func(*args,**kwargs)
        print("step 5: exiting decorater3.wrapper (iner layer)")
        result-=10
        return result
    return wrapper

@decorater1
@decorater2
@decorater3
def add(a,b):
    print("step 4: executing original function (inside of decorater 3)")
    return a+b

if __name__=="__main__":
    print("=== Calling add(10, 5) ===")
    result = add(10, 5)
    print("step 8: Final result returned:", result)