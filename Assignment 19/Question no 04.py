'''
Write a pYTHON script t print unique digit of a given integer

'''
x = input("Enter a number:")
i=0
for y in x:
    if x.index(y)==i:
        print(y,end="")
    i+=1
print()