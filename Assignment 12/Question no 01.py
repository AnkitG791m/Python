'''
Write a python script to check whethe given number is positive or non-positive.

'''

x = int(input("Enter a positive or negative number:"))
if x>0:
    print(f"{x} is positive number")
elif x==0:
    print(f"{x} Zero")
else :
    print(f"{x} is negative value")