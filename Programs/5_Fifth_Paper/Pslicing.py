# l = [1,2,3,4,5,6,7,8,9,10,11]
# n = 2
# for i in range(0, len(l)-1, n*2):
#     l[i], l[i+1] = l[i+1],l[i]
# print(l)

# #[[1], 1, 3, 4, [5], 5, 7, 8, [9], 9] not given L
# # [2, 1, 3, 4, 6, 5, 7, 8, 10, 9]

# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n = input("Enter the letter: ")
# n ='ABCDF'
# str1 =""
# for i in n:
#     str1 += chr(ord(i)+1)
    
# print(str1)



# a = 15
# c = ""
# for i in range(a+1):
#     # if i > 0:
#     c += str(i)
# print(c.count("1")) 
        

# s = "vinayakhavannavar"
# s = list(s)
# n = 2
# for i in range(0,len(s)-1,n*2):
#     s[i], s[i+1] = s[i+1], s[i]    
# print(''.join(s))
    

# s = 'Msys Technologies PVT Ltd'
# str1 = ''
# for i in s:
#     # if i.islower():
#     #     print(i)
#     if 'A'<= i <= 'Z':
#         str1+= 
# print(str1)
        

# a = "Msys Technologies PVT Ltd"
# b = " "
# low = a.lower()
# for i in low:
#     if i == " ":
#         b += "_"
#     else:
#         b += i
# print(b)


# a = "#Msys@Technologies.com$"
# str1 = ''
# low = a.lower()
# for i in low:
#     if i in '!@#$%^&*.,':
#         str1 += " "
#     else:
#         str1 += i
# print(str1)

# a = "#Msys@Technologies.com$"
# str1 = ' '
# upr = a.upper()
# for i in upr:
#     if i in '!@#$%^&*,.':
#         str1 += " "
#     else:
#         str1 += i
# print(str1)

# s = 'Vinayak Havannavar'
# p = s[11:12:1]
# print(p)

# s = 'Vinayak Havannavar'
# a = s[:7:-1]
# b = s[7::-1]
# c = a + b
# print(c)

# s = 'Vinayak Havannavar'
# for i in range(len(s)):
#     print(i, ":", s[i])

# s = 'Vinayak Havannavar'
# p = s[0:6]      # "Vinaya"
# p = s[0:3]      #Vin   
# p = s[-1:-3]    # ""
# p = s[-3:-1]    #"Va"
# p = s[-3:0]     # ""
# p = s[0::2]     # "VnykHvnaa"
# p = s[3:3]      # ""
# p = s[3:4]      # "a"
# p = s[-5:-2]    # "nav"
# p = s[::-2]     # "rvnaa aai"
# p = s[:4]       # "Vina"
# p = s[-3:]      # "var"
# p = s[::-1]     # "ravannavaH kayaniV"
# print(p)


# a = "#Msys@Technologies.com$"
# c = 0
# str = ""
# # for i in range(len(a)):
# #     print(i,":", a[i])
# for i in a:
#     # print(i)
#     if i == 'e':
#         c += 1
#         str += ' '
#     else:
#         str += i

# print(f'Charector count is: {c}')
# print(f'Charector replaced by space: {str}')


# for i in a:
#     if i == "e":
#         str += "s"
#     else:
#         str += i
# print(str)

s = 'aaabbbssseee'
c = 0
j = 1
for i in s:
    if i == s[j]:
        # print(s[j])
        c +=1