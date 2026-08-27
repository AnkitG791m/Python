'''
Write a python script to print first N odd natural numbers.

'''
print("Printing first n odd naatural numbers")
n=int(input('Enter the value of N:'))
j=1
for i in range(1,n*10,2):
    print(i)
    if j==n:
        break
    j+=1

