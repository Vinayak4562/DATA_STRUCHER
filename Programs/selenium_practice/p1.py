# import sys

# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = x + y
# print(f'Result z = {z}')

# # PS D:\CODES\OJT_ASSIGNMENT\Programs\selenium_practice> python .\p1.py 3 4
# # Result z = 7


l = ["abc", "def"]
c = " "
# for i in range(len(l[0])):
#     c += l[0][i] + l[1][i]
# print(c)

for i in range(max(len(l[0]), len(l[1]))):
    if 0 < len(l[0]):
        c += l[0][i]
    if 0 < len(l[1]):
        c += l[1][i]

print(c)
