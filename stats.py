def count(text):
    x = text.split() 
    return len(x)

def countChar(text):
    counts = {}
    text = text.lower()
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(dict_item):
    return dict_item["num"]

def getSortedList(char_dict):
    sorted_list = [] 
    
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            sorted_list.append(new_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list