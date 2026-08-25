'''
Write a python script to make a menu drive program in which user has to choose one of the option from four given:
1 Odd - Even
2 Positive - NOn Positive
3. Simple interest
4. Roots of quadratic equaton.

'''
choice = int(input("1. Odd - Even\n2. Positive - Ne Inon Positive\n3. Simplterest\n4. Roots fo quadratic Equation\nEnter your choice"))
match choice:
    case 1:
        x = int(input("Enter a number:"))
        if x%2==0:
            print(f"Its Even Number")
        else:
            print(f"Its Odd Number")
    case 2:
        x = int(input("Enter a positive or negative number:"))
        if x>0:
            print(f"{x} is positive number")
        elif x==0:
            print(f"{x} Zero")
        else :
            print(f"{x} is negative value")   
    case 3:
        principle_amount = int(input("Enter your invested amount:"))
        rate_of_intrest = 5.25 # percent
        invested_time = int(input("For how long did you invest? - "))
        intrest = ((principle_amount*rate_of_intrest)*(invested_time/12))/100
        print(f"The total intrest in rupee is {intrest}")
        print(f"Your final amount is {principle_amount+intrest}")   
    case 4:
        print("Enter the Quadratic equation like ax^2+bx+c=0")
        a,b,c = int(input("Enter Value of A:")),int(input("Enter Value of B:")),int(input("Enter Value of C:"))
        d=b**2-(4*a*c)
        if d>0:
            print("This is real & Distinct root")
        elif d==0:
            print("This is real & Equal root")
        else:
            print("This is imaginary roots")               