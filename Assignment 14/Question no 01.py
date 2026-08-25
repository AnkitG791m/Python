'''
Write a python script to check whether a given number is a three digit number or not.

'''
x = int(input("Enter Number"))
match x:
    case x if (x>99 and x<1000):
        print("This is 3 Digit number")
    case _:
        print("This is not 3 digit number")
    