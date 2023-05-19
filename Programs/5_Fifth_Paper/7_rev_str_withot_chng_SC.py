'''7. Reverse the below string without changing the position of special characters .
s = "adfw$vf&yvy*ugv%uy"
'''

# my_string = "adfw$vf&yvy*ugv%uy" 
# # my_string =  input("Enter the combination of char and special char: ")
# lst = list(my_string)
# left = 0
# right = len(lst) - 1

# while left < right:
#     if not lst[left].isalnum():
#         left += 1
#     elif not lst[right].isalnum():
#         right -= 1
#     else:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1

# result = ''.join(lst)
# print(f'Reverse the given string without changing the position of special char: {result}')

# Input:- my_string = "adfw$vf&yvy*ugv%uy" 
# Output:- Reverse the given string without changing the position of special char: yuvg$uy&vyf*vwf%da

# import string

# s = "adfw$vf&yvy*ugv%uy"
# l1 = list(s)
# left = 0
# right =len(l1)-1
# while left < right:
#     if l1[left].isalpha() and l1[right].isalpha():
#         l1[left],l1[right] = l1[right],l1[left]
#         left+=1
#         right-=1
#     elif l1[left] in string.punctuation:
#         left+=1
#     elif l1[right] in string.punctuation:
#         right-=1
# result = "".join(l1)
# print(f'Reverse the given string without changing the position of special char: {result}')

s = "abc$ef#-!ab@de"
res = " "
res1 = ""
res_rev= ""
re = "!@#$%^&*~-"
for i in s:
    if i in re:
        res1 += i
    else:
        res += i        
print(f'Alphabets: {res}')
print(f'Special Charecter: {res1}')
for j in res:
    res_rev = j + res_rev
print(f'Reversed Alphabets: {res_rev}')

i , j = 0,0
output = ""
for k in s:
    if k in res_rev:
        output += res_rev[i]
        i+=1
    else: 
        output += res1[j]
        j += 1
print(f'Out Put: {output}')


# #---------------------------------------------------------------------
# char = ""
# sp_char = ""
# count = 0
# reverse = ""
# for i in s:
#     count += 1
# print(count)
# for j in s:
#     if j in "!@#$%^&*()-":
#         sp_char += j
#     else:
#         char += j
# print(char)
# print(sp_char)

# for k in char:
#     reverse = k + reverse
# print(reverse)

#---------------------------------------------------------------------
   


   
   
      

