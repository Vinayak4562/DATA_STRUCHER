'''18. dct = {111: "Eric", 112: "Kyle", 113: "Butters"} Load the above dictionary variable in a 
file 'test.txt' . Now create a new dictionary variable (eg. dct2) and load the contents of the file 
'test.txt' in it. Print the value of key '112' using the new dictionary variable .
Note : Use pickling for solving this question.
O/p : Kyle
'''

import pickle

dct = {111: "Eric", 112: "Kyle", 113: "Butters"}        # create the original dictionary

with open("test.txt", "wb") as f:                       # write the dictionary to a file using pickling
    pickle.dump(dct, f)

with open("test.txt", "rb") as f:                       # load the dictionary from the file using pickling
    dct2 = pickle.load(f)

print( f'The value of key 112 is: {dct2[112]}')         # access the value of key '112' in the new dictionary
