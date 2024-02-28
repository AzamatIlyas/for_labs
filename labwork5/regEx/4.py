import re
txt = input()
x = re.findall(r"[A-Z][a-z]+",txt)
print(x)
