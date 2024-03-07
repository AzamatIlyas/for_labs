import os
def copy(file1,file2):
    with open(file1,'r') as f1:
        with open(file2,'w') as f2:
            f2.write(f1.read())
a = input()
b = input()
copy(a,b)