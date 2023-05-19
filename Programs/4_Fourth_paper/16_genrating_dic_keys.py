'''16. Let’s consider there are two files, one file contains testnames, other file contains testnames and status for each one. Generate a dictionary with key’s as testname and value as status.
Input : 
    FiIe1.txt: 
test1 
test2
    File2.txt: 
test1-pass 
test2-fail


Output : { "test1" : "pass", "test2" : "fail"}
'''

with open('.\\OJT_ASSIGNMENT\\Programs\\Fourth_paper\\16_generating_dic_keys\\file1.txt', 'r') as f1:      # read test names from File1.txt
    # test_names = [line.strip() for line in f1]
    test_names = f1.readline().strip()


test_statuses = {}                      # read test statuses from File2.txt and generate dictionary
with open('.\\OJT_ASSIGNMENT\\Programs\\Fourth_paper\\16_generating_dic_keys\\file2.txt', 'r') as f2:
    for line in f2:
        name, test_names = line.split('-')
        test_statuses[name] = test_names.strip()

print(test_statuses)                    # print the resulting dictionary
