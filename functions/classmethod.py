class A:
    school_name="RCM"
    def __init__(self,data):
        self.data=data
        pass

    @classmethod
    def class_method(cls,value):
        print("from class method")
        print(value,"is best language in the world")
        print(cls,"current refering class")
        print(type(cls))
        # cls.self.data=value
        # print("modified value=",cls.self.data)

    @classmethod
    def change_school(cls,new_name):
        cls.school_name=new_name

a=A(10)
a.class_method("python")  
print("curent school name",A.school_name)
A.change_school("ABC")
print("changed school name",A.school_name)
a.change_school("XYZ")
print("school name changed with object reference",a.school_name)