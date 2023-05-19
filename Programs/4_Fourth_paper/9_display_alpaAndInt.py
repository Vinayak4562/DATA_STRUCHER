'''9. Given a string “abcde”, Display the output as “a1b2c3d4e5”'''

str_ing = input("Enter the alphabets: ")
result = ""
num = 0
for i in range(len(str_ing)):
    result += str_ing[num]
    num += 1
    result += str(num)
print(result)

# Input: abcde
# OutPut:a1b2c3d4e5