'''10. Generate a dictionary from the two given lists using dict function (without using for loops) and calculate the sum of all the values in the dictionary using reduce and anonymous concepts
L1 = [“a”,”b”]	L2 = [1,2] 
Expected Output : 
data = {“a'.1, “b'.2} sum = 3
'''

from functools import reduce

def dict_function(l1,l2):
    # data = dict(zip(l1,l2))
    data = {l1[i] : l2[i] for i in range(len(l1))}
    sum_values = reduce(lambda x,y : x+y,data.values())
    return f'data:{data}, Sum of values are: {sum_values}'
    
print(dict_function(l1 = ["a","b"],l2 = [1,2]))
#OutPut: data:{'a': 1, 'b': 2}, Sum of values are: 3