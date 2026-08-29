'''
Write a python script to calculate sum of cubes of first N natural numbers.

'''
print("Printing first N natural numbers Cubesc sum")
n=int(input('Enter the value of N:'))
sum=0
for i in range(1,n+1,1):
    sum=sum+(i**3)

print(sum)