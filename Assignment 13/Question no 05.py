'''
Write a python script to print greater among threee numbers. 
print number only once even if the number are the sam e.

'''
print("Enter X y z :")
a,b,c=int(input()),int(input()),int(input())
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"{c} is greater than {a} and {b}")
else:
    print(f"All numbers are same that is {a}")

          