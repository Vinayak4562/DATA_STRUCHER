n = int(input("Enter the number: "))
s = "*"                          # making asterisk as string
for i in range(1, n+1):          # this for loop runes from 1 to n+1 number of times
    if i % 2 == 0:               # if i is equal devisible by 2 then only it will print the num in reverse order
        s += str(i)              
        r = s[::-1]
        print(r)
    else:                        #  else it will print the *
        s += str(i)
        print(s)
 
# Input:- Enter the number: 3
# Output pattern:-
# *1 
# 21*
# *123

