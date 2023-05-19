'''5.From a given list of numbers, create a list of squares of prime numbers .
l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
'''

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# list1 = [1, 4, 6, 11, 15, 24, 19, 25, 27, 30, 17]
# # list1 = [int(i) for i in input("Enter a list of numbers separated by spaces: ").split()]

# prime_squares = []
# for num in list1:
#     if is_prime(num):
#         prime_squares.append(num ** 2)
# print(f'list of squares of prime numbers: {prime_squares}')


l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
l2 = []
for i in l1:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                print(j , end = " ")
        
