#Write a python script to swap data of two variables
 ## Method 1
    #Usign third variable
print("\t\tSwapping two number using third variable")
x,y=10,20
print(f"The previos value in x is {x} and in y is {y}")
z=x
x=y
y=z

print(f"After the swaping x is {x} and y is {y}\n\n\n")

## method 2
    #without using third variable
print("\t\tSwapping two number without using third variable")
x,y=10,20
print(f"The previos value in x is {x} and in y is {y}")
x=x+y #10+20=30
y=x-y #30-20=10
x=x-y #30-10=20
print(f"After the swaping x is {x} and y is {y}\n\n\n")

print("\t\tSwapping two number using xor operator")
x,y=10,20
print(f"The previos value in x is {x} and in y is {y}")
x=x^y # 10^20 = 01010 ^ 10100 = 11110 = 30
y=x^y # 30^20 = 11110 ^ 10100 = 01010 = 10
x=x^y # 30^10 = 11110 ^ 01010 = 10100 = 20
print(f"After the swaping x is {x} and y is {y}")