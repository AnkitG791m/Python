'''
Write a python script to print cubes to first N natural numbers
'''
n=int(input("Enter the Value of N:"))
i=1
j=1
while j<=n:
    print(i)
    j+=1
    i=j
    i**=3

    