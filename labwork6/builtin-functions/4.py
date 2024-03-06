import time
import math
def sqrt(a, b):
    time.sleep(b/10)  
    result = math.sqrt(a)
    return result

a = int(input("number: "))
b = int(input("which milliseconds after you want see result: "))
result = sqrt(a, b)
print(f"Square root of {a} after {b} milliseconds is {result}")