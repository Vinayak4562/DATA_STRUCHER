'''11. From the given list, check if the element is an integer then return the square of that element 
and if element is a string then return the same string 2 times. Output should be in list format.
a = [8,9,10,"f",5,8,"d"]
Output should be : [64, 81, 100, 'ff', 25, 64, 'dd']
a = [8,9,10,"f",5,8,"d"]
'''
a = [8,9,10,"f",5,8,"d"]
# a = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
# lst = []
# for x in a:
#     if isinstance(x, int):
#         lst.append(x**2)
#     else:
#         lst.append(x*2)
# print(f'Square of an Integer and double of string: {lst}')



a = [8,9,10,"f",5,8,"d"]
output = [(lambda x: x ** 2 if isinstance(x, int) else x * 2)(element) for element in a]
print(f'Square of an Integer and double of string: {output}')

# input:- a = [8,9,10,"f",5,8,"d"]
# output:- Square of an Integer and double of string: [64, 81, 100, 'ff', 25, 64, 'dd']