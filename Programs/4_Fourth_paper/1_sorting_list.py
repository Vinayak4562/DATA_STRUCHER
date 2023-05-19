# 1. Sort the below list without using inbuilt function I = [2,3,-5,-7,9,4,6,-1,-8,0]

l = [2,3,-5,-7,9,4,6,-1,-8,0]

list1 = []
i = 0
j = 1
for i in range(len(l)): 
    for j in range(i+1, len(l)):          
        if l[i] <= l[j]:
            j += 1           
        else:
            l[i],l[j]=l[j], l[i]
            j += 1
print(l)
