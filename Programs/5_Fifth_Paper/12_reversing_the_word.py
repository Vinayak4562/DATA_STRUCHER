'''12. Write a Python Program to Reverse the Content of a File.
Input :-
I am
new to this
world of
Python.
Output :-
Python.
world of
new to this
I am
'''

# filename = 'input.txt'
with open('input1.txt', 'r') as f:
    lines = f.readlines()  # Read all lines of the file
print(f'Original input: {lines}')

lines.reverse()  # Reverse the list of lines


with open('output1.txt', 'w') as f:
    f.writelines(lines)  # Write the reversed lines to a new file
print(f'Reversed Output: {lines}')