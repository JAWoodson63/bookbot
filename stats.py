def num_of_words(text):
    word_list = text.split()
    return len(word_list)

def num_of_characters(text):
    chars = {}
    for char in text:
        ch = char.lower()
        if ch in chars:
            chars[ch] = chars[ch] + 1
        else:
            chars[ch] = 1
    return chars