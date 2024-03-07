def cases(a):
    upper11 = 0
    lower11 = 0

    for i in a:
        if i.isupper():
            upper11+=1
        elif i.islower():
            lower11+=1
    return upper11,lower11

word = input("Input here : ")
upper,lower = cases(word)
print(upper,lower)