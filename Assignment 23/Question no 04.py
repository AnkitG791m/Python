'''
Write a python script to print binary equivalent of a give decimal number. 
(Do not use bin() method)
'''
a=25
s=''
while a!=0:
    s=str(a%2)+s
    a//=2

print(s)