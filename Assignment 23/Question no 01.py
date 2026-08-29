'''
Write a python script to calculate factorial of given number.

'''
n=int(input("Enter the value of n:"))
fact=n
for i in range(n,1,-1):
    n-=1
    fact=fact*(n)
    if n==1:
        break
print("Factorial of n is ",fact)