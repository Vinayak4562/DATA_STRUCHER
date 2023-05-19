# def my_gen(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1

# # for val in my_gen(3):
# #     print(val)

# g = my_gen(3)
# print(next(g))
# print(next(g))
# print(next(g))
# ---------------------------------------------------------

# gen = (i+i for i in range(5))
# for i in gen:
#     print(i)

# ------------------------------------------------------------
'''7. Reverse the below string without changing the position of special characters .
s = "adfw$vf&yvy*ugv%uy" '''

s = "adfw$vf&yvy*ugv%uy" 
# p = ""
# re = '!@#$%^&*'
# for i in s:
#     if i not in re:
#         p+= i
#         # q = p[::-1]
#     else:
#          for j in p:
#              if j not in re:
#                  new = j[::-1]
#     print(new)
            
    # q = p[::-1]
# print(p)
# print(q)

    # else:
    #     print(p)
# q = p[::-1]


# s = "adfw$vf&yvy*ugv%uy"
# res_alpha= "" 
# special_char = ""
# res = ""
# for i in s:
#     if i.isalpha():
#         res_alpha += i
#         special_char +=" "
#     else:
#         res_alpha+= " "
#         special_char += i

# print(res_alpha)
# print(special_char)
# # for k in special_char:
# #     new_character = k.split(" ")
# #     print(new_character)
     

# new_alpha = res_alpha.split(" ")
# print(new_alpha)
# new_character = special_char.split(",")
# print(new_character)

# for j in new_alpha:
# #         res += j[::-1]+
# # print(res)

#     result = list(zip(new_alpha[::-1],new_character))
# print(result)


# new = res_alpha.split(" ")
# print(new)
# print(res)
# for j in new:
#     a = j[::-1]
#     print(a)
    # if j != new:


s = "adfw$vf&yvy*ugv%uy"
re = '!@#$^&*' 
s.split(re)
char = []
sp_char = []
for i in s:
    if i not in re:
        char.append(i)
print(char)