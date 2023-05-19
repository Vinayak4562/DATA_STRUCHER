
# def binary_search(lst,target):
#     start = 0
#     end = len(lst)-1
#     while start <= end:
#         mid =  (start + end) // 2
#         if lst[mid] == target:
#             return f'Index Value is: {mid}'
#         elif target > lst[mid]:
#             start = mid + 1
#         elif target < lst[mid]:
#             end = mid - 1

# lst1 = [1,2,3,4,5,6,7,8,9]
# print(binary_search(lst1,1))  



# n = 10000
# count = 0
# while n > 0:
#     if n % 10 == 0:
#         count += 1
#     n = n // 10
# print(count)

##--------------- count_zeros using Recursion ------------
# def count_zeros(n, c):
#     if n > 0: 
#         if n % 10 == 0:
#             return count_zeros(n//10, c+1)
#     return c
# print(count_zeros(10000, 0))

##--------------- count_zeros using Recursion ------------
# def count_zeros(n):
#     if n > 0: 
#         if n % 10 == 0:
#             return 1+count_zeros(n//10)
#     return 0
# print(count_zeros(1000))




##--------------- sum_dig using While loop ------------

# n = 234
# sum = 0
# while n > 0:
#     num = n % 10
#     n = n // 10
#     sum += num 
# print(f'the sum of all Digits: {sum}')

##--------------- sum_dig using Recursion ------------
# def sum_dig(n, sum):
#     if n > 0:
#         num = n % 10
#         n = n // 10
#         sum += num
#         return sum_dig(n, sum)
#     return sum

# print(sum_dig(234,0))

##--------------- add_ele from list using for loop ------------
# lst = [1,2,3,4]
# sum = 0
# for i in lst:
#     sum += i
# print(sum)
##--------------- add_ele from list using Recursion ------------
# def add_ele (n,i ,sum):
#     if i < len(n):
#         return add_ele(n,i+1,sum+n[i])
#     return sum
# n = [1,2,3,4]
# print(add_ele(n,0,0))



##--------------- getting second largest ele from list using for loop ------------

# lst = [1,2,3,4,6,5,5,5,6,6,6]
# first =  0
# second = 0
# for i in lst:
#     if i > first:
#          second = first
#          first = i
#     elif i > second and i < first:
#         second = i        
            
# print(f'First largest:{first}')
# print(f'Second Largest: {second}')


##---------------getting second largest ele from list using Recursion ------------
# def second_largest(lst,i=0,first=0,second=0):
#     if i == len(lst):
#         return second 
       
#     if lst[i] > first:
#         second = first
#         first = lst[i]

#     elif lst[i] > second and lst[i] < first:
#         second = lst[i]
      
#     return second_largest(lst, i+1, first, second)

# lst = [1,2,3,4,6,5,5,4,3,6,14,12,10,13]
# print(second_largest(lst))




##--------------- printing privius digit if its None using for Loop------------
# lst = [None, None, None,1,None,None,None, 2,None,None, 3, None]
# for i in range(len(lst)):
#     if lst[0] == None:
#         lst[0] = 0
#     if lst[i] == None:
#         lst[i]=lst[i-1]
# print(lst)

##---------------printing privius digit if its None using for Loop builtin mehod------------
# lst = [None, None, 1,None,None,None, 2,None,4,None, 3, None, None]
# lst1 = []
# dig = 0
# for i in range(len(lst)):
#     if lst[i] != None:
#         dig = lst[i]
#     if lst[i] == None:  
#         lst1.append(dig)
#     else:
#         lst1.append(lst[i])
# print(lst1)


##--------------printing privius digit if its None using WHILE Loop------------
# lst = [None, None, 1,None,None,None, 2,None,4,None, 3, None, None]
# lst1 = []
# j = len(lst)   # j=11
# dig = 0
# i = 0
# while i < j:
#     if lst[i] != None:
#         dig = lst[i]
#     if lst[i] == None:  
#         lst1.append(dig)
#     else:
#         lst1.append(lst[i])
#     i += 1
# print(lst1)

##--------------- using Recursion ------------
# def replace_None(lst, i=0, dig = 0):
    


# lst = [1,None,None, 2,None,None, 3, None]
# print(replace_None(lst))


##-------------------- Fibonacy------------------------
# num = 10
# a = 0
# b = 1

# for i in range(num):
#     print(a, end = " ")
#     c = a + b
#     a = b
#     b = c

##-------------------- Fibonacy------------------------

# n = 10
# a = 0
# b = 1
# lst = []
# ele = 5
# for i in range(n):
#     lst.append(a)
#     # print(a)
#     c = a + b
#     a = b
#     b = c
# # print(lst)
# for j in lst:
#     if j == ele:
#         print(lst[j])
#         break
#     else:
#         print("Element Not Found")

##-------------------- Fibonacy using Recursion ------------------------
# def test(target):
#     num = 10
#     a = 0
#     b = 1
#     lst = []
#     for i in range(num):
#         lst.append(a)
#         c = a + b
#         b = a
#         a = c    
#         # print(lst)  # lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for j in range(len(lst)):
#         if lst[j] == ele:
#             return f'index number of given elment is: {j}'                  
#     return f'Element not found'

# ele = int(input("Enter the Element: "))      
# print(test(ele))


##-------------------- Counting Number of alphabets------------------------
# s = 'aabbccc24ddd'
# i = 0
# l = len(s)  #12
# res = ""
# while i < l:    
#     s1 = s[i]
#     if '0' <= s1 <= '9':
#         res += s1
#         i += 1
#     else :
#         c = 1
#         j = i + 1
#         while j < l and s1 == s[j]:
#             c += 1
#             j += 1
#         res += s1
#         res += str(c)
#         i = j
# print(res)




##-----------------------Palindrome using While loop not working-----------------------------------------
# pal = "malayalam"
# f = 0
# l = len(pal)-1
# c = 0
# while f < l:
#     if pal[f] == pal[l]:
#         c += 1
#         f += 1
#         l -= 1
#     else:
#         break

# if c == (len(pal)// 2):
#     print("Its a pal")
# else:
#     print("Not a pal")
    

    
##-----------------------Palindrome using for loop not working------------------------------------------
# pal = 'liril'
# f = 0
# l = len(pal)-1
# c = 0
# for i in range(len(pal)):
#     if pal[i] == pal[j]:
#         l -=1
#         f += 1
#         c += 1
#     else:
#         break
# if c == (len(pal)//2):
#     print("Its a Palindrome")
# else:
#     print("Its not a Palindrome")
    
#------------------------------------------------------------------------------------------

#---------------------------Even or Odd---------------------------------------------
# num = 4
# if num%2 ==0:
#     print("its a even number")
# else:
#     print("its a odd number")

# num = [0,1,2,3,4,5,6,7,8,9,0]
# even =[]
# odd = []
# for i in num:
#     if num[i] != 0:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)        
#     else:   
#         print("Zero Devision Error")
# print(even)
# print(odd)

# def even_odd(num):
#     even =[]
#     odd = []
#     for i in range(len(num)):
#         if num[i] != 0:
#             if num[i] % 2 == 0:
#                 even.append(num[i])
#             else:
#                 odd.append(num[i]) 
                       
#         else:   
#             return f"Zero Devision Error"
#     return even,odd

# num = [1,2,3,4,5,6,7,8,9]      
# print(even_odd(num))


# num = int(input("Enter the number: "))

# print("even" if num % 2 == 0 "odd")
# print(res)


# a = round(3.5)
# print(a)
# b =round(0.5)
# print(b)
# c = round(0.6)
# print(c)
# d= round(3.4)
# print(d)


# n = 10
# a = 0
# b = 1
# i = 0
# while i < n:
#     print(a)
#     c = a + b
#     b = a
#     a = c
#     i += 1


# def fibonacci(n):
#     a=0
#     b=1
#     if n<0:
#         print("incorrect")
#     elif n==0:
#         return 0
#     elif n==1:
#         return b
#     else:
#         for i in range(1,n):
#             c=a+b
#             a=b
#             b=c
#         return b
# print(fibonacci(9))

##------------------------ Factorial While loop-------------------------------------

# f = 1
# n = 10
# i = 0
# while i < n:
#     i +=1
#     f = i * f    
# print(f)
##------------------------ Factorial recursion-------------------------------------

# def factorial(n,f = 1, i=0):
#     if i < n:
#         i += 1
#         f = i * f
#         return factorial(n ,f,i)
#     else:
#         return f

# print(factorial(3,1,0))




##------------------------ Factors While loop-------------------------------------
# fact = 10
# i = 1
# lst = []
# while i <= fact:    
#     if fact % i == 0:
#         lst.append(i)
#     i += 1
# print(lst)  #lst= [1, 2, 5, 10]

##------------------------ Factors recursion-------------------------------------

# def fact_rec(fact,i):
#     if i <= fact:
#         if fact % i == 0:
#             print(i)
#         fact_rec(fact,i=i+1)       
# fact_rec(10,i=1)

##------------------------ GCD While loop-------------------------------------

# fact = 10
# i = 1
# lst = []
# while i <= fact:    
#     if fact % i == 0:
#         lst.append(i)
#     i += 1
# # print(lst)  #lst= [1, 2, 5, 10]

##------------------------------------Need to be work-------------------------------------------

# str = "11234"
# s = 1
# p = 1
# for i in str:
#     res = i*p

#     print(res)
#     # if res == s:
#     #     print("its a color full num")
#     # else:
#     #     print("its not a color full num")


##-------------------------------------------------------------------------------------------------


string="vishal"
vowels="aeiouAEIOU"
string=list(string)
i,j=0,len(string)-1
while i<j:
    if string[i] not in vowels:
        i+=1
    if string[j] not in vowels:
        j-=1
    string[i],string[j]=string[j],string[i]
    i+=1
    j-=1
print(''.join(string))


