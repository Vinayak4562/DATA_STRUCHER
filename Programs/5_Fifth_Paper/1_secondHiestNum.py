'''1. Write a program in Python to find the second highest number 
in an integer array without using inbuilt functions.'''

# create an array of integers
arr = [10, 20, 4, 45, 99, 200, 30]
# arr = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]
max_num = arr[0]
second_max = arr[0]

for i in range(len(arr)):       # loop through the array to find the maximum and second maximum numbers
    
    if arr[i] > max_num:        # update the maximum number if the current number is greater than the maximum
        second_max = max_num
        max_num = arr[i]

    elif arr[i] > second_max and arr[i] != max_num:      # update the second maximum number if the current number is greater than the second maximum
        second_max = arr[i]

print("The second highest number is:", second_max)      # print the second maximum number