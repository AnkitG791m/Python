'''
Write a python scipt to print first 10 multiples of n
'''
print("\t\tPrinting Multiples of N")

n=int(input("Enter the value of n:"))
for i in range(n,(n*10+1),n):
    print(i)