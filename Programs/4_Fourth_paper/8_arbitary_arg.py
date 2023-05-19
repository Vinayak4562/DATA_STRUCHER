'''8. What is the return type of arbitrary positional arguments and arbitrary keyword arguments'''

'''In Python, arbitrary positional arguments are represented using the syntax *args 
and arbitrary keyword arguments are represented using the syntax **kwargs.
The return type of these arguments depends on the implementation of the function. 
Since these arguments can be of any type and can have any number of elements, the return type can also vary.
In general, functions that accept *args and **kwargs typically operate on the values passed in and return some 
computed value, such as a number, a string, a list, or a dictionary.
For example, consider the following function that accepts arbitrary positional and keyword arguments and 
returns their sum:'''

def add_values(*args, **kwargs):
    total = sum(args)               # add all the positional arguments
    for value in kwargs.values():
        total += value              # add all the keyword arguments
    return f'Addition of all the values are: {total}'

print(add_values(10,20,30,40))
# Output: Addition of all the values are: 100