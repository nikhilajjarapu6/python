class A:
    def __init__(self,*args):
       if len(args)==1:
           self.area=args[0]**2
       elif len(args)==2:
           self.area=args[0]*args[1]
       elif len(args)==3:
            a, b, c = args
            if (a + b <= c) or (a + c <= b) or (b + c <= a):
                raise ValueError("Invalid triangle sides")
            s = (a + b + c) / 2
            self.area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

       else :
             raise ValueError("Invalid number of arguments")
           
square = A(20)
print("area of square", square.area)

rect = A(10, 20)
print("area of rectangle", rect.area)

tri = A(10, 20, 25)
print("area of triangle", round(tri.area, 2))
