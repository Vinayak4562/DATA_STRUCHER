'''8. Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. 
For eg., if the credit card no. is “4509876278910046”, then function should return “************0046”.'''
# def hide_card_number(card_number):
    
#     num_length = len(card_number)               # Get the length of the card number       
#     hidden_chars = '*' * (num_length - 4)       # Replace all characters except the last four with asterisks    
#     masked_number = hidden_chars + card_number[-4:]     # Concatenate the hidden characters with the last four digits    
#     return f'Last four digits of your card Number is: {masked_number}'

# card_number = '1234567812345678'
# # card_number = int(input("Enter the card number which has to be masked: "))
# masked_number = hide_card_number(card_number)
# print(masked_number)  # Output: *****6789




# card_No = '4509876278910046'
# def card():
#     card_No = input("Enter the card Number: ")

#     num = len(card_No)
#     star = num - 4
#     number = card_No[-4:]
#     str = star*"*"
#     str += number
#     return str

# masked = card()
# print(f'Your masked Card Number is: {masked}')

card_No = '4509876278910046'
length = len(card_No)
res = " "
for i in range (length):
    if i < length - 4:
        res += "*"
    else:
        res  += card_No[i]
print(res)