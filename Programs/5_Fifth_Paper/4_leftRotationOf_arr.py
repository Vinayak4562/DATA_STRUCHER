'''4.Write a Python program to perform left rotation of array elements by two positions.'''

# def rotate_right(arr):
    
#     temp_lst = arr[:2]                      # Store the first two elements in a temporary list    
#     for i in range(2, len(arr)):            # Shift all the other elements by two positions to the left
#         arr[i-2] = arr[i]    
#     arr[-2:] = temp_lst                     # Copy the temporary list to the end of the array

#     return f'Right rotation of array elements by two positions: {arr}'

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# # arr = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
# print(f'Original Array Befor performing the rotation: {arr}')
# print(rotate_right(arr))

def rotate_left(arr):
    
    temp_lst = arr[-2:]                     # Store the last two elements in a temporary list    
    for i in range(len(arr)-3, -1, -1):     # Shift all the other elements by two positions to the left
        arr[i+2] = arr[i]    
    arr[:2] = temp_lst                      # Copy the temporary list to the beginning of the array

    return f'Left rotation of array elements by two positions: {arr}'

arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
print(f'Original Array Before performing the rotation: {arr}')
print(rotate_left(arr))


