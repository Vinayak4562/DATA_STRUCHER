'''4. Define a function which returns dictionary that stores the words and it’s length from the given text
text = “Be happy”
Expected Output : {“Be'.2,”happy”:5}'''


def dict_word(text):
    a = text.split()
    dict1 = {}
    for i in a:
        dict1[i] = len(i)
    return dict1

text = input("Enter a list of numbers separated by spaces: ")
print(dict_word(text))