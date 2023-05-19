user_1 = input("enter : ")
user_2 = int(input("enter : "))

try:
    print(user_1 + user_2)
except TypeError:
    print("cannot concatenate string and number")


input = ("user1",)
output = ("password",)
res = input+output
print(res)

# enter : 'vinayak
# enter : 456
# cannot concatenate string and number
# ('user1', 'password')


