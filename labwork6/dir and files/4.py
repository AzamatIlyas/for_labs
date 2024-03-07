import os 
x = input()
f = open(x, 'r') as file
line_sum = sum(1 for line in file)
print(line_sum)