import os 
x = input()
print(os.listdir(x))
for i in os.listdir(x):
    if os.path.isdir(x):
        print(i)
for j in os.listdir(x):
    if os.path.isfile(x):
        print(i)