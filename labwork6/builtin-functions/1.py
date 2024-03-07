import operator
import functools

def multiply(a):
    result = functools.reduce(operator.mul,a)
    return result

arr = [int(i) for i in input("list a: ").split()]
print(multiply(arr))