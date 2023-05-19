'''3.Write Python Program to delete element from array at given index.'''

def delete_at_index(arr, index):         # check if index is within array bounds
   
    if index < 0 or index >= len(arr):
        print("Index out of range!")
        return arr
    else:        
        new_arr = arr[:index] + arr[index+1:]       # create a new array with the element at the given index removed
        return new_arr


arr = [1, 2, 3, 4, 5]
# arr = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
index_num = int(input("Enter the index number which val vill be delete:"))
new_arr = delete_at_index(arr, index_num)
print(f'List Before deleting the element: {arr}')
print(f'List After deleting the element: {new_arr}')
