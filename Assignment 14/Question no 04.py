'''
Write a python script to take one data form user and evaluate the type of data. 
if the data is of int type then print monday,
if the data is of float type the pritn tuersday,
if the data is complex type thenprint wednesday,
if the data is of type bool then print thursday.

'''
x=eval(input("Enter here"))
match x:
    case x if type(x)==int:
        print("Int type data")
    case x if type(x)==float:
            print("Float type data")
    case x if type(x)==complex:
            print("Complext type data")
    case x if type(x)==bool:
            print("bhool type data")
    
    case _:
            print("Data type not found")