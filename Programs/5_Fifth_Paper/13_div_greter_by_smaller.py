'''13. Write a python program to take 2 inputs(numbers) from the user. 
Divide the greater number by the smaller number. Validate the user inputs, it should be integer type only . 
If the input is not integer, raise an exception and catch it. Also, if the divisor is 0, 
catch the exception raised.
try:
'''
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    if num1 > num2:
        result = num1 / num2
    else:
        result = num2 / num1

    print("Result:", result)

except ValueError as e:
    print("Invalid input:", e)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
