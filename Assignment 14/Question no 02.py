'''
Write a python script to check whether a given number is positive, negative or zero.

'''
x = int(input("Enter number:"))
match x:
    case x if x>0:
        print("Its positive number")
    case x if x<0:
        print("Its negative number")
    case _:
        print("Its Zero")