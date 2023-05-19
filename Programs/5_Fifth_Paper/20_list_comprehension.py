'''20. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by 
any single digit besides 1 (2-9).'''

result = [num for num in range(1, 1001) if any(num % div == 0 for div in range(2, 10))]

print(result)