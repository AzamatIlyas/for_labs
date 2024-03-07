import os 
x = input()
if os.path.exist(x):
    os.remove(x)