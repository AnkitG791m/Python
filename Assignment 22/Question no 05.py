'''
Write a python script to calculate sum of first n even natural numbers.
'''
print("Printing first n even natural numbers sum")
n=int(input('Enter the value of N:'))
sum=0
j=1
for i in range(2,n*10,2):
    sum=sum+i
    if j==n:
        break
    j+=1
print(sum)
