# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""

# your code here

"""
password = str(input("Enter password "))
for letter in password:
    if letter.islower:
        #has at least one lowercase letter
        for letter in password:
            if letter.isupper:
                #has at least one uppercase letter
                for letter in password:
                    if letter.isdigit:
                        print("The password is secure.")        
                    else:
                        print("The password is insecure!")
            else:
                print("The password is insecure!")
    else:
        print("The password is insecure!")
"""

cap=0
low=0
dig=0
password = str(input("Enter password "))
for symbol in password:
    if ('A' <= symbol <='Z'):
        cap+=1
    if ('a' <= symbol <= 'z'):
        low+=1
    if (symbol.isdigit()):
        dig+=1
if (cap!=0 and low!=0 and dig!=0):
    print("The password is secure!")
else:
    print("The password is insecure!")
