# PYTHON PROGRAM WHICH SHOWS THE LARGEST AMONG THREE NUMBERS, IF NOT THEN SMALLEST 
while True:   
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    num3=int(input("Enter the third number: "))
    if num1==num2 and num1==num3:
        print("All the numbers are same.")
    elif num2==num1 and num2==num3:
        print("All the numbers are same.")
    elif num3==num1 and num3==num2:
        print("All the numbers are same.")
    elif num1==num2 and num1>num3:
        print(f"{num3} is the smallest.")
    elif num1==num3 and num1>num2:
        print(f"{num2} is the smallest.")    
    elif num2==num3 and num2>num1:
        print(f"{num1} is the smallest.")
    elif num1>num2 and num1>num3:
        print(f"{num1} is greatest among all three numbers.")
    elif num2>num1 and num2>num3:
        print(f"{num2} is greatest among all three numbers.")
    elif  num3>num1 and num3>num2:
        print(f"{num3} is greatest among all three numbers.")
    ask=input("Do you want to use this program again(yes/no): ")
    if ask == "yes":
        continue
    else:
        print("Thank you for using this program!")
        break
