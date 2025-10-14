def validate(a,b):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float))):
         raise TypeError("Both inputs must be numbers")