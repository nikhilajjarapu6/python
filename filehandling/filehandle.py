import pdfplumber 

file_path="D:/Program Collection/Python/filehandling/helloworld.txt"
result=open(file_path)
# print(result.read())

file_path="D:/Program Collection/Python/filehandling/text.txt"
with open(file_path) as file:
    content=file.read()
print("="*50)   

#returns linen by line in file
with open(file_path) as f:
    print(f"reading one line......",f.readline())
    print(f"reading second line......",f.readline())
    print(f"reading third line......",f.readline())
    
print("="*50)
#read line by line
with open(file_path) as f:
    for i,line in enumerate(f):
        if i%2==0:
            print(line)

print("="*50)
with open(file_path) as f:
    for line in f:
        print(line.strip())

# Count lines, words, and characters in a file
print("="*50)
with open(file_path) as f:
    content = f.read(5)
    lines = content.split('\n')
    words = content.split()
    chars = len(content)
    
    print(lines)
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {chars}")

print("="*50)
search="PDF"
with open(file_path) as f:
    for i,line in enumerate(f,start=1):
        print(f"reading line {i}:{line.strip()}")
        if search.lower() in line.lower():
            print(f"{search} is line {i}:{line.strip()}")

print("="*50)
# second=open("second.txt","x") to create files x, a for if file alredy exixt
rev_path="second.txt"
with open(file_path) as f:
    lines=f.readlines()
    print(lines)

# with open(rev_path,"w") as f:
#     f.writelines(reversed(lines))
#     print(f.tell())
#     f.seek(0)
#     print(f.read())
    

  



    





