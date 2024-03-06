def char(a):
    b = 0
    c = 0
    for i in range(len(a)):
        if a[i] != " ":
            char = a[i]
            if char.isupper():
                b+=1
                i+=1
            elif char.islower():
                c+=1
                i+=1
        else:
            i+=1
    print(f"{b} , {c}")
        
a = str(input())
aa = char(a)