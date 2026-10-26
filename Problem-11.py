def contains_vowel(som: str) -> bool:
    vowels = set('aeiou')
    for i in som:
        if i in vowels:
            return True
    return False
print(contains_vowel("hello"))
# Output: True
# Output: False