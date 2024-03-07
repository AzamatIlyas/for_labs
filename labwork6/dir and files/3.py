import os 
x = input()
if os.path.exist(x):
    name = os.path.basename(x)
    name2 = os.path.dirname(x)
print(name, name2)