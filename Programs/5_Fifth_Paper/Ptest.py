# l = [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]
# dict1 = {}
# for i in l:
#     if i % 2 == 0:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1
# print(dict1)
    

# a = int(input("Enter the first num: "))
# b = int(input("Enter the second num: "))
# res = 0
# while a > 0:    
#     res += b
#     a -=1
# print(res)


# s = '121134'
# str1 = ""
# for i in s:
#     if i not in str1:
#         str1 += i
#         res = list(str1)
#         # print(res)
# res1 = 0
# for i in res:
#     res1 += int(i)
# print(res1)


# l1 = ['a', 'b', 'c','d']
# l2 = [1,2,3,4]
# l3 = []
# for i in range(len(l1)):    
#     p = l1[i]
#     q = l2[i]
#     l3.append(p)
#     l3.append(q)
# print(l3)

# s = 'a,man,nama'
# f = 0
# l = len(s)-1
# c = 0
# w = ""
# p = s.split(",")
# print(p)
# for i in p:
#     w += i
# print(w)
# for i in p:
#     if i[f] == i[l]:
#         c += 1
#         f += 1
#         l -= 1
#     else:
#         break

# if c == (len(s)// 2):
#     print("Its a pal")
# else:
#     print("Not a pal")




# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = []
# for i in range(len(l1)):    
#     p = l1[i]
#     q = l2[i]
#     c = p + q
#     l3.append(c)
# print(l3)


l = [1,4,3,6,2,9,7]
f = 0
s = 1
maximum = 0
minmum = 0
while len(l) < 0:
    if l[f] <= l[s]:
        maximum = l[f]
        f +=1
        s +=1
    else:
        minmum = l[s]
        f +=1
        s +=1
print(maximum)
print(minmum)