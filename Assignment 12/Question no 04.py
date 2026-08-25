'''
Write a python script to print greater between two numbers. 
Print number onlyu once e en if the number are the same

'''
x = int(input("Enter the first num:"))
y = int(input("Enter the second num:"))
if x>y:
    print(f"{x} is greater than {y}")
elif x==y:
    print(f"{x} and {y} is Equal")
else:
    print(f"{y} is Greater than {x}")