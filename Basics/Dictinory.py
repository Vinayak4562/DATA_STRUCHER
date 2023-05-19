this_dict =	{"brand": "Ford", "model": "Mustang", "year": 1964 }

# # To get all key names in the dictionary, one by one.
# for i in this_dict:
#   print(i, end = " ")   # brand model year return Type is String
# print(type(i), end = " ")        # <class 'str'>


# # To get all values in the dictionary, one by one.
# for i in this_dict:
#   print(this_dict[i])    #Ford  Mustang  1964

# #You can also use the values() function to return values of a dictionary:
# for i in this_dict.values():
#   print(i)              #Ford  Mustang  1964

#  Loop through both keys and values, by using the items() function:
for i in this_dict.items():
  print(i)
print(type(i)) # ('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)  return type is Tuple <class 'tuple'>