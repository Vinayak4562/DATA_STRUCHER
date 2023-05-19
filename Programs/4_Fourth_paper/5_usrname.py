'''5. Let’s consider there is a list which contains usernames, 
You have received requirement to add one more username to the list (without using append and assignment approaches) 
input : [“user1”,”user2”]
output : [“user1”,”user2”,”user3”]
'''
# def  add_user(a):
#     list1 = ["user1","user2"]
#     list1.extend(a)
#     return list1
# print(add_user(["user3"]))


def  add_user(a):
    list1 = ["user1","user2"]
    return list1.__add__(a)

print(add_user(["user3"]))


# Output:['user1', 'user2', 'user3']