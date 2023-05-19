'''6. Define the logic for generating the email id based on username and department 
Get the username and department as a input and create a email id from it
input : username : msys 
        department: automation
Output: msys.automation@gmail.com
'''

username = input("Enter the username: ")
department = input("Enter the department: ")
print(f'{username}.{department}@gmail.com')

res = username +"."+department +"@gmail.com"
print(res)

# Enter the username: msys
# Enter the department: automation
# msys.automation@gmail.comS