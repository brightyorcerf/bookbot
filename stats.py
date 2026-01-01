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
