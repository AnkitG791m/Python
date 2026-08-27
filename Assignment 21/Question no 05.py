'''
write a python script to display all prime nubmers within a range 
# range start =15 end = 45
'''
start,end=15,45
print("Printing all prime number beetwen 15 to 45")
for i in range (start,end):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(f"{i} is prime nubmer")
