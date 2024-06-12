def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
user_reply = True

num1 = float(input("Enter the first number: "))

while user_reply:
    num2 = float(input("Enter the second number: "))
    for op in operations:
        print(op)
    operation_symbol = input("Pick an operation from the above list: ")
    calculation = operations[operation_symbol]
    sol = calculation(num1, num2)
    print(sol)
    if input("Do you want to continue? y/n: ") == "y":
        num1 = sol
    else:
        user_reply = False


