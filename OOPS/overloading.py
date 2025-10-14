import platform
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c    #overrides previous one
    def add(self,a,b=0,c=0):  #default values
        print(a+b+c)
    def add(self,*args):
        print(f"args {args}")
        print(f"sum ={args[0]+args[1]}")  
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            print(a+b)
        elif isinstance(a, str) and isinstance(b, str):
            print(a + " " + b)
        else:
            return None
    

if __name__=="__main__":
    a=A()
    # print(a.add(1,2))    #error
    a.add(10,20)
    # a.add(10)          #in add method we get exception becuase accesing through index[1] is nothing here
    # a.add(10,20)
    a.add("hello","world")
    print(platform.architecture())
    print(platform.machine())
