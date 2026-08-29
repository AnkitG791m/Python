'''

Write a python script to print the octal equivalent of a given decimal number.
(Do not use oct() method)
'''
a=25
s=''
while a!=0:
    s=str(a%8)+s
    a//=8

print("The octal number is ",s)