'''19.Define a generator to print the numbers between o to n (including) which are divisible by 5 
and should be even N = 20 Output : 10 20
'''

def div_by_5_even(n):
    for i in range(0, n+1, 10):
        if i % 2 == 0:
            yield i

number = int(input("Enter the number: "))

# for num in div_by_5_even(number):
#   print(f'Even number that divisible by 5 is: {num}')
lst = []
for num in div_by_5_even(number):
    lst.append(num)
print(f'Even number that divisible by 5 is: {lst}')

