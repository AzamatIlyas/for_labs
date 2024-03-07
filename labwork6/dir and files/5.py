import os 
x = input()
y = ['a', 'b', 'c']
f = open(x, 'w')
f.write(y)
f.close()
f.open(x, 'r')
print(f.read(x))