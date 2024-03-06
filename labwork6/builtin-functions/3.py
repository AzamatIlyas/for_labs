def polindrom(a):
    a1 = a[::-1]
    if a1 == a:
        return "yes"
a = input()
aa =  polindrom(a)


if aa == "yes" :
    print("YES, this word is polindrom")
else:
    print("NO, this word is not polindrom")