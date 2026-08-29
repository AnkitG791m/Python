'''
Write a python script to calculate sum of digits of a given number.
'''
x= int(input("Enter a number:"))
sum=0
temp=x%10
while x>0:
    sum = sum+temp
    x//=10
    temp = x%10
print(sum)