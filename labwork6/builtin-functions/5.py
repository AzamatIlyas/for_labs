def elements(elements):
    return all(elements)


a = tuple(map(int,input("tuple a: ").split(" ")))
print(a)
print(elements(a))