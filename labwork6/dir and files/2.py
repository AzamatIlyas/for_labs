import os 
x = input()
if os.path.exist(x):
    print('yes')
if os.acces(x, os.R_OK):
    print('yes')
if os.acces(x, os.W_OK):
    print('yes')
if os.acces(x, os.X_OK):
    print('yes')