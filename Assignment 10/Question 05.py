'''
Write  a python script which takses a three digit number from the user 
and displays only its middle digit.
'''

x = int(input("Enter the three digit number:"))
temp = x
x =x//10
x = x%10
print(f"The Middle number of {temp} is {x}")