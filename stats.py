def num_word(text):
    return len(text.split())

def letter_count(text):
    dict = {}
    for letter in list(text.lower()):
        if letter not in dict:
            dict[letter] = 0
        dict[letter] += 1
    return dict

def sortby(things):
    return things["num"]

def sortedlist(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True, key=sortby)
    return list