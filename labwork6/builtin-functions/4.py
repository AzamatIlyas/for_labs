import time
import math
def jjj(a, b):
    time.sleep(b/1000)  
    result = math.sqrt(a)
    return result

a = int(input("Number : "))
b = int(input("Milliseconds : "))
result = jjj(a, b)
print(result)