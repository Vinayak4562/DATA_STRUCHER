'''6. Read a given file and extract the integers from each line, concatenate all the integers present in the same line and print the sum of all these integers.
eg: <File content>
He is 32 yrs old and his son is 7 yrs old .
She is 27 yrs old and her daughter is 2 yrs old .
Output : 599 ## calculation : Integers on Line 1 + Line 2 = 327 + 272 = 599
'''
with open("file1.txt", "r") as file:
    total_sum = 0
    for line in file:
        line_sum = 0
        for word in line.split():
            if word.isdigit():
                line_sum += int(word)
        total_sum += line_sum
print(f'Total sum of all the digits: {total_sum}')


# He is 32 yrs old and his son is 7 yrs old.
# She is 27 yrs old and her daughter is 2 yrs old.
# Out_put:-Total sum of all the digits: 68



