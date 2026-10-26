text = input("input your word:")
def separate_by_indix(word):
    cat = ()
    text_even = ''
    text_odd = ''
    for i in range(0, len(word)):
        if i % 2 == 0:
            text_even = text_even + word[i]
        else:
            text_odd = text_odd + word[i]
    cat = text_even, text_odd
    print(cat)
separate_by_indix(text)
# Output: ('Hloel', 'elWrd')