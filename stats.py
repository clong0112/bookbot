def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    num_words = len(text.split())
    return num_words

def char_dict(text):
    word_list = (text.lower().split())
    char_dict = {}
    for word in word_list:
        for c in word:
            char_dict[c] = 1 + char_dict.get(c, 0)
    return char_dict

def sort_into_list_of_dict(charDict):
    def sort_on(items):
        return items["num"]
    res = []
    for k, v in charDict.items():
        res.append({"char": k, "num": v})
    res.sort(reverse=True, key=sort_on)
    return res