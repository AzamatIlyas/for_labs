def word(a):
    a = a.lower().replace(" ","")
    if a == a[::-1]:
        print("yes")
    else:
        print("no")
d = input("Here : ")
word(d)