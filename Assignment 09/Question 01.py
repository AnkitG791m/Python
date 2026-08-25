# Write a python script to calcutlate simple intrest.
principle_amount = int(input("Enter your invested amount:"))
rate_of_intrest = 5.25 # percent
invested_time = int(input("For how long did you invest? - "))
intrest = ((principle_amount*rate_of_intrest)*(invested_time/12))/100
print(f"The total intrest in rupee is {intrest}")
print(f"Your final amount is {principle_amount+intrest}")