'''
Write a python script to pirnt table of user's choice.

'''
print("\t\tPrinting Table of Your Choice")
j=1
n=int(input("Enter the number :"))
for i in range(n,(n*10+1),n):
    print(f"{n} x {j} = {i}")
    j+=1