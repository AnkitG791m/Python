"""
Create two python file a0.py and a1.py . Create a variable in A1.py and assign some value to it.
write a python script to import A1 module in a0 and print value of the variable created in a0.py

print a from a0.py calling by a1.py

"""
import a1
import a0
c = a0.a + a1.b
print("Sum all a and b is",c)

