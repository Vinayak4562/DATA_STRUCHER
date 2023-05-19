import  random

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special_char = "!@#$%^&*"
n= int(input("Enter digit to generate Password: "))
password=''
for i in range(n):
    password+=random.choice(caps+small+number+special_char)
print(f'Your Password is:',password)

# Enter digit to generate Password: 9
# Your Password is: tzLTlu0%!
