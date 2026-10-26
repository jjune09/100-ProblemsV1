word = ["hello", "world", "test", "case", "example"]

def charecter_frequency(*args):
    word_dict = {}
    for i in args:
        for j in i:
            for k in j:
                if k in word_dict:
                    word_dict[k] = word_dict[k] + 1
                else:
                    word_dict[k] = 1
    print(word_dict)
charecter_frequency(word)
# Output: {'h': 1, 'e': 4, 'l': 5, 'o': 3, 'w': 1, 'r': 2, 'd': 2, 't': 3, 'c': 2, 'a': 3, 's': 3, 'x': 1, 'm': 1, 'p': 1}