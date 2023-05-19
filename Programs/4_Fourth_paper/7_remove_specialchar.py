'''7 In the given string, remove the special characters and add a space instead of that 
“Msys&Technologies@Chennai'''

def remv_spl(a):
    result = ""
    for i in string1:
        if i in "!@#$%^&*.":
            result += " "
        else:
            result += i
    return result 

string1 = input("Enter the string that containing specail char: ")
print(remv_spl(string1))

# Input: Enter the string that containing specail char: Msys&Technologies@Chennai      
# OutPut:Msys Technologies Chennai