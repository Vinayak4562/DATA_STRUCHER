'''2. Define a function which returns a list contains only the palindrome strings from the list of
provided string elements.

input	: List of strings
output : List of palindrome strings'''

def pal_string(string1):
    palindromes = []
    for string in string1:
        if string == string[::-1]: # Check if the string is equal to its reverse
            palindromes.append(string)
    return palindromes

string1 = input("Enter a strings separated by spaces: ").split()
print("List of palindromes are:",pal_string(string1))

# Enter a strings separated by spaces:hi its nitin met with liril they spoke in malayalam
# List of palindromes are: ['nitin', 'liril', 'malayalam']