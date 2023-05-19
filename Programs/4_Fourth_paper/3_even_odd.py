'''3 Define logic for identifying the even numbers and odd numbers from the given list and 
generate a dictionary as follows
numbers = [4,5,7,2,9,8]
result	= {“even”:[4,2,8],”odd'.[5,7,9]}'''

even = []
odd = []
num = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
result = dict({"even": even,"odd" : odd})
print(result)
# Enter a list of numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# {'even': [2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}
