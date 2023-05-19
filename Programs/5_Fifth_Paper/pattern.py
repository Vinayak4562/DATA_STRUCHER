#--------------------------------------------------------------------

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()

# #         * 
# #         * * 
# #         * * *
# #         * * * *
# #         * * * * *
#--------------------------------------------------------------------
# n = 4 
# for i in range(n,0,-1):
#     for j in range(1, i+1):
#         print("*", end = " ")    
#     print()

# #         * * * * 
# #         * * * 
# #         * *
# #         *
# #--------------------------------------------------------------------

# n = 4 
# for i in range(n):
#     for j in range(1+i):
#         print("*", end=" ")
#     print()

# #        * 
# #        * * 
# #        * * *
# #        * * * *

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()
#--------------------------------------------------------------------
# n = 5 
# for i in range(n):
#     for j in range(i , n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# #         * 
# #       * * 
# #     * * *
# #   * * * *
# # * * * * *
#--------------------------------------------------------------------
# n = 5
# for i in range(n):
#     for j in range(n, i, -1):
#         print("*", end=" ")
#     print() 

##      * * * * *
##      * * * *
##      * * *
##      * *
##      *

#--------------------------------------------------------------------
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(n, i, -1):
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(i, n):
#         print("*", end = " ")
#     print()
    
# #   * * * * * 
# #     * * * * 
# #       * * *
# #         * *
# #           *    

#--------------------------------------------------------------------
# n = 5
# for i in range(n):
#     for j in range(i, n):         # decreasing
#         print(" ", end=" ")
#     for j in range(i):            # increasing
#         print("*", end =" ")
#     for k in range(i+1):          # increasing
#         print("*", end =" ")
#     print()

#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

# n = 5
# for i in range(n):
#     for j in range(i, n):         # decreasing
#         print(" ", end=" ")
#     for j in range(i):            # increasing
#         print("*", end =" ")
#     for k in range(i+1):          # increasing
#         print("*", end =" ")
#     print()

#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

#--------------------------------------------------------------------
# n = 5
# for i in range(n):
#     for j in range(i +1):         # increasing
#         print(" ", end=" ")
#     for j in range(i, n-1):       # decreasing 
#         print("*", end =" ")
#     for j in range(i, n):         # decreasing 
#         print("*", end =" ")  
#     print()

# #   * * * * * * * * * 
# #     * * * * * * * 
# #       * * * * *
# #         * * *
# #           *   


# #--------------------------------------------------------------------
# n = 4
# for i in range(n):
#     for j in range(i +1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print(" ", end =" ")
#     print()
    
# for i in range(n-1):
#     for j in range(i, n-1):
#         print("*", end =" ")
#     print()

# #    *
# #    * *
# #    * * *     
# #    * * * *
# #    * * *
# #    * *
# #    *

# #--------------------------------------------------------------------
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i+2):
#         print(" ", end=" ")
#     for k in range(i,n-1):
#         print("*", end=" ")
#     print()

# #         * 
# #       * * 
# #     * * * 
# #   * * * * 
# #     * * * 
# #       * * 
# #         * 

# #--------------------------------------------------------------------
# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end =" ")
#     for k in range(i):
#         print("*", end = " ")
#     for l in range(i+1):
#         print("*", end = " ")
#     print()

# for i in range(n-1):
#     for j in range(i+2):
#         print(" ", end =" ")
#     for k in range(i,n-2):
#         print("*", end = " ")
#     for l in range(i,n-1):
#         print("*", end = " ")
#     print()

##---------------------------------------------------

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(i, n):
#         print("*", end=" ")
#     print()

# min = 0


# list1= [2233,83,123456,97]
# result = {}
# for i in list1:
#     new = str(i)
#     n = len(new)//2
#     key = int(new[n:])
#     value = int(new[:n])
#     result[key] = value
# print(result)

# text = "be happy"
# text1 = text.split(" ")

# print(text1)
# word_length = {}
# for i in text1:
#     word_length[i] = len(i)
# print(word_length)

# from functools import reduce
# l1 = ["a","b"]
# l2 = [1,2]
# data = {l1[i]:l2[i] for i in range(len(l1))}
# print(data)
# result = reduce(lambda x,y : x+y,data.values())
# print(result)
# n = 5

# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(i,n-1):
#         print("*", end=" ")
#     for k in range(i,n):
#         print("*", end=" ")
#     print()
        
print(str.maketrans({'a':'b'}))


