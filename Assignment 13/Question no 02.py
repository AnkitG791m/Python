'''
Write a python script to check whether a given number is positive, negative or zero.

'''
x = int(input("Enter a positive or negative number:"))
if x>0:
    print(f"{x} is positive number")
elif x==0:
    print(f"{x} Zero")
else :
    print(f"{x} is negative value")