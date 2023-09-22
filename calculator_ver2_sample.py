def calculate(num1, num2, todo):
    if todo == '+':
        result = num1 + num2
    elif todo == '-':
        result = num1 - num2
    elif todo == '*':
        result = num1 * num2
    elif todo == '/':
        result = num1 / num2
    elif todo == '**':
        result = num1**num2
    else:
        print("Error, you have to choose an operation")
        return

    print(f"Result = ", result)


number_1 = float(input("Write a number 1: "))
number_2 = float(input("Write a number 2: "))

print("Select the operation on the numbers and enter the corresponding sign into the console")
print(' 1) Add +\n 2) Subtract -\n 3) Multiply *\n 4) Divide /\n 5) Raise to a power **\n')

operation = str(input("Write an operation: "))

calculate(number_1, number_2, operation)