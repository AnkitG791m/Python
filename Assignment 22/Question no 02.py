'''
Write a python script to calculate sum of squares of first Natural numbers
'''
print("Printing first N natural numbers Square sum")
n=int(input('Enter the value of N:'))
sum=0
for i in range(1,n+1,1):
    sum=sum+(i**2)
print(sum)