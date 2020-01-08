from .func import *


print('''
1. Vocabulary
2. Contacts''')
chose = input(int('What you wanna to do?'))

if chose == 1:
    wordadd()
elif chose == 2:
    contactadd()
