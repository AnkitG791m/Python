'''
Write a python script to check whether a given quadratic equation has two real
& distinct root, real & equal roots or imaginary roots
'''
print("Enter the Quadratic equation like ax^2+bx+c=0")
a,b,c = int(input("Enter Value of A:")),int(input("Enter Value of B:")),int(input("Enter Value of C:"))
d=b**2-(4*a*c)
if d>0:
    print("This is real & Distinct root")
elif d==0:
    print("This is real & Equal root")
else:
    print("This is imaginary roots")