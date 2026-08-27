'''
Write a python script to print firest M multiple of N.

'''
print("\t\tPrinting first M multiples of N")
n=int(input("Enter the value of N:"))
m=int(input("Enter the value on M:"))
for i in range(n,n*m+1,n):
    print(i)
