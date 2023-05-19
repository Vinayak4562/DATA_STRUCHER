'''14. In the given list, check if the element is None, replace it with the recent value .
l = [1,None,None,3,None,4]
Output should be : [1,1,1,3,3,4]
'''

l = [1,None,None,3,None,4]
recent_value = None
for i in range(len(l)):
    if l[i] is not None:
        recent_value = l[i]
    else:
        l[i] = recent_value

print(l)
