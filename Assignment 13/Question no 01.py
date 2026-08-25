#Write a python script to check whether a given number is a three digit number or not.
a= int(input("Enter number:"))
if a>99 and a<1000:
    print(f"{a} is three digit number")
else:
    print("A is not three digit")