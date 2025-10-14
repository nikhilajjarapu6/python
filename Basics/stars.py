n=8
print("...........................")
for i in range(1,n+1):
    print('*'*i)

print("......................")
for i in range(n,1,-1):
    print("*"*i)

print("......................")

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

print("......................")
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(i+(i-1)))

print("......................")
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(i+(i-1)))

print("......................")
for i in range(1,n+1):
    print(' '*(n-i)+"*"*i)