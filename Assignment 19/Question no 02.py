'''
Write a python script to print only vowels of the given string

'''
count =0
x= "I am Ankit G"
y ="aeiouAEIOU"
for a in x:
    if a in y:
        print(a)
        count+=1
print(count)
       