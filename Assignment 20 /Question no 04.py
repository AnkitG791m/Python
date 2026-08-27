'''
Write a python script to print the first 10 multiples of  in reverse order.

'''
print("\t\tPrinting first M multiples of N in Reverse order")

n=int(input("Enter the value of N:"))
m=int(input("Enter the value on M:"))
for i in range(m*n,n,-n):
    print(i)
