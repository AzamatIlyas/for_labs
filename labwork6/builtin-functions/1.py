from functools import reduce

def multiply(a):
    result = reduce(lambda x, y: x * y, a)
    return result

a = [int(i) for i in input("list a: ").split()]
print(f"result: {multiply(a)}")