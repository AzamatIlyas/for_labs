import os 
def jj(way):
    with open(way,'r') as file:
        line_sum = sum(1 for i in file)
    return line_sum
ggg = input()
print(jj(ggg))