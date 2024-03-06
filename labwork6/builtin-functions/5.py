def true_elements(elements):
    return all(elements)


a = tuple(map(int,input("tuple a: ").split(" ")))
print(a)
print(f"{a} {true_elements(a)}")