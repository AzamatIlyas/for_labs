import os 
x = input()
f = open(x, 'r')
y = f.read(x)
f.close()
d = open('copy', 'w')
d.write(y)
d.close()