# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""

# your code here

"""
text = str(input("Enter text "))
cap = 0
for letter in text:
    if letter.isupper():
        cap = cap + 1

print("Number of capital letters in text is ", cap)
"""

text = str(input("Enter text "))
cap = 0
for letter in text:
    if ('A' <= letter <='Z'):
        cap = cap + 1
print("Number of capital letters in text is ", cap)