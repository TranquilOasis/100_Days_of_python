# Day 5 - Python Loops
"""
Password Generator
"""
import random

l = int(input("How many letters would you like in your password?"))
s = int(input("How many symbols would you like?"))
n = int(input("How many letters would you like?"))

numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
letters = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

password = []
lchosen = 0
schosen = 0
nchosen = 0
for i in range(l + s + n):
    rchoice = random.choice(["l", "s", "n"])
    if rchoice == "l" and lchosen <= l:
        password.append(random.choice(letters))
        lchosen += 1
    if rchoice == "s" and schosen <= s:
        password.append(random.choice(symbols))
        schosen += 1
    if rchoice == "n" and nchosen <= n:
        password.append(random.choice(numbers))
        nchosen += 1

print(f"Your password is: {''.join(password)}")