def remove_word(sentence: str, word_to_remove: str) -> str:
    words = sentence.split()
    filtered_words = [word for word in words if word != word_to_remove]
    return ' '.join(filtered_words)
sentence = "Python is a popular programming language."
word_to_remove = "popular"
print(remove_word(sentence, word_to_remove))    