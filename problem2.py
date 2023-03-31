def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return num1, num2, operator

def displayResult():
    num1, num2, operator = takeInput()

    if operator == '+':
        result = num1 + num2
        formula = f"{num1} + {num2} = {result}"
    elif operator == '-':
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    elif operator == '*':
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero")
            return
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        print("Invalid operator")
        return

    print(formula)

displayResult()