"""
cryptography.py
Author: Ella Edmonds
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
a = input('Enter e to encrypt, d to decrypt, or q to quit: ')

if a != "q" and "e" and "d":
    print("Did not understand command, try again.")

if a == "q":
    print("Goodbye!")
    
if a == "e" or "d":
    b = input ("Message: ")
    c = input ("Key: ")
    
'''associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

associations.find(char)

associations[index]'''

