'''
Write a python script which takes a three digit nubmer from the uer and displayes'
only its first digit

'''
print("\t\tPrinting first digit")
x=int(input("Enter 3 digit number:"))
y=x//100
print(f"The first digit of {x} is {y}")