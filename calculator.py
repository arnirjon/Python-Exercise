#Calculator with python

while True:    
    choose = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")

    if choose == '1':
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        Addition = first_number + second_number
        print("The sum is:",Addition)

    elif choose == '2':
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        Subtraction = first_number - second_number
        print("The difference is:",Subtraction)
    
    elif choose == '3':
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        Multiplication = first_number * second_number
        print("The product is:",Multiplication)
    
    elif choose == '4':
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        Division = first_number / second_number
        print("The quotient is:",Division)
    
    elif choose == '5':
        break
    
    else:
        print("Error")