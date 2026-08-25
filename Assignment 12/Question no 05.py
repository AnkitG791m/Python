'''
Write a python script to print two given words in dictionay order.

0'''

x = input("Enter first letter:")
y = input("Enter second letter:")

if x<y:
    print(f"{x} \n {y}")
else:
    print(y,x,sep="\n")


