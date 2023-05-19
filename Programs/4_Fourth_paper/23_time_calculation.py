'''23.Write a logic for calculating the time taken for executing the python function'''

import time

def add(a, b, c=0):
    return a + b + c

start_time = time.time()             # Record the start time using time.time method
print(add(5, 4))
print(add(5, 4, 5))                  # Calling the function
end_time = time.time()               # Record the end time using time.time method
time_taken = end_time - start_time   # Calculate the time difference

print(f"Time taken for function execution: {time_taken:.4f} seconds")

