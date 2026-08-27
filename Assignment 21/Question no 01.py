'''
Write a python script to print first N even natural numbers.

'''
print("Printing first n even naatural numbers")
n=int(input('Enter the value of N:'))
j=1
for i in range(2,n*10,2):
    print(i)
    if j==n:
        break
    j+=1

