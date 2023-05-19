'''29. Find the element in a list using Binary Search Algorithm and return a tuple 
containing the element and its index.'''

def binary_search(arr, target): # arr: A sorted list of elements and target: The target element to search for
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return (arr[mid], mid) # it return: A tuple containing the target element and its index in the list, or None if not found.
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1    
    return None  # If the target element is not found in the list, return None.


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]       
target = int(input("Enter the element which index to be to be search: "))     

result = binary_search(arr, target)
if result:
    print(f"Target element {result[0]} found at index {result[1]}.")
else:
    print("Target element not found.")


# Outputs:-
# Enter the element which index to be to be searched:4
# Target element 4 found at index 3.
# Enter the ele which index to be to be searched: 10
# Target element not found.