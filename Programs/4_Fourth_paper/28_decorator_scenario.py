def handle_zero_division(func):
    def wrapper(num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        else:
            return func(num1, num2)
    return wrapper

@handle_zero_division
def divide(num1, num2):
    return num1 / num2

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result1 = divide(a,b)
print(f'result of {a} divided by {b} is: {result1}')  # returns 5.0
# Enter the value of a: 10
# Enter the value of b: 2
# result of 10 divided by 2 is: 5.0

# Enter the value of a: 10
# Enter the value of b: 0                   # raises ZeroDivisionError
# raise ZeroDivisionError("Cannot divide by zero!")
# ZeroDivisionError: Cannot divide by zero!
