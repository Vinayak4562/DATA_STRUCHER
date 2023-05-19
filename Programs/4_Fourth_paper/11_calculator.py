'''11.Define the calculater logic in such a way that addition and substraction function should be in one python file and
multiplication should be in another python file access these functions and utilize them inside the main file.'''

from  add_sub import addition,subtraction
from mul_div import multiplication, division

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Addition of a and b is:",(addition(a,b)))
print("Subtraction of a and b is:",(subtraction(a,b)))
print("Multiplication of a and b is:",(multiplication(a,b)))
print("Division of a and b is:",(division(a,b)))

# Enter the value of a: 3
# Enter the value of b: 2
# Addition of a and b is: 5
# Subtraction of a and b is: 1
# Multiplication of a and b is: 6
# Division of a and b is: 1