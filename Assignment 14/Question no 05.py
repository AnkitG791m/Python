'''
Write a python script to take a string form the suer. 
if the string is a part of "mysirg"
the print"One"
if the string is a part of educaton then print"two"
and if the string is a part of "Services" then print "Three"
'''
x=input("Enter string")
match x:
    case x if x in "mysirg":
        print("One")
    case x if x in "education":
        print("two")
    case x if x in "services":
        print("three")


