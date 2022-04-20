print("Input the two numbers.")
a = int(input("First number: "))
b = int(input("Second number: "))
print("Input the operator (+, -, *, /). For exit, input 0.")
x = input("Operator: ")

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Zero on a second argument. Division isn't impossible."
    else:
        return a / b

while True:
    if x == "0":
        break
    else:
        if x == "+":
            print("Result:", plus(a, b))
        if x == "-":
            print("Result:", minus(a, b))
        if x == "*":
            print("Result:", multiplication(a, b))
        if x == "/":
            print("Result:", division(a, b))
        print("Input the two numbers.")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Input the operator (+, -, *, /). For exit, input 0.")
        x = input("Operator: ")
