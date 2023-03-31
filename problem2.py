# start  
def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")
    return num1, num2, op

def displayResult():
    num1, num2, op = takeInput()

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    formula = f"{num1} {op} {num2}"
    print(f"{formula} = {result}")

displayResult()
