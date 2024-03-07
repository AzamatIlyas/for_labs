import os 
def write(name,list):
    with open(name,'w') as file:
        for i in list:
            file.write(str(i)+"\n")
file = input()
arr = [str(i) for i in input("Input list : ").split()]
write(file,arr)