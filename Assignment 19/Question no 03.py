'''
Write a python script to count occurrence of spaces in given string
'''
count = 0
x = input("Enter a string:")
for a in x:
    if a==" ":
        count+=1
print("The total space in this string is ", count)