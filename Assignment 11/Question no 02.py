'''
Write a python script to input two strings from the user and 
display whether the two variables referred to same oject or not . print  true or false

'''
x = input("Enter first string:")
y = input("Enter second string:")
print(id(x) is id(y))