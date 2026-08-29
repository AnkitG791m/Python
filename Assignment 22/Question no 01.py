'''

Write a python script to calculate sum of first n natural nubmers.
'''
print("\t\tPrinting first n natural numbers sum")
n = int(input("Enter the value of N:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
