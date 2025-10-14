def lambda_func():
    x=lambda a,b:a+b  #lambda directly retuned
    return x
func=lambda x,y:x*y
# print(func(10,20))
# print(func.__name__)

students=[("alice",22),("bob",24),("charlie",23),("rock",21)]

def get_age(student):
    print(student)
    return student[1]

print(type(students))
sorted_students=sorted(students)  #based on key
sorted_age=sorted(students, key=get_age)   #sorted function iterate internally
sorted_lambda=sorted(students,key=lambda student:student[1], reverse=True) 
name_lamda=sorted(students,key=lambda x:x[0])


if __name__=="__main__":
    # print(lambda_func()(10,20))
    print(students)
    print(sorted_students)
    print(sorted_age)
    print(sorted_lambda)
    print(name_lamda)