'''2. Write a program in Python to remove duplicate elements from an array without using inbuilt function.'''

def remv_dupl(arr): 
    
    unique = []                 # this empty list is use to store unique elements    
    for i in arr:               # this for loop will iterate over each element in the array
        
        if i not in unique:     # check if the element is not already in the unique list
            
            unique.append(i)    # add the element to the unique list
    
    return f'List of Unique Elements: {unique}' 


arr = [1, 2, 3, 4, 3, 4, 5, 6, 7, 7, 7, 8]
# arr = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]

unique_arr = remv_dupl(arr)     # call the remove_duplicates function

print(unique_arr)
