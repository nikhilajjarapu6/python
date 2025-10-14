from utils.validate import validate
from utils import math


def calculate(a,b,operation):
    validate(a,b)

    if operation=="add":
        result=math.add(a,b)
        print(f"{a}+{b}= {result}")
    elif operation=="sub":
        result=math.sub(a,b)
        print(f"{a}-{b}= {result}")
    elif operation=="mul":
        result=math.mul(a,b)
        print(f"{a}*{b}= {result}")
    elif operation=="div":
        result=math.div(a,b)
        print(f"{a}/{b}= {result}")
    else:
       raise ValueError("Unknown operation")
    