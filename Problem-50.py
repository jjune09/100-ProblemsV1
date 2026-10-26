from typing import List

def find_words_of_length(words: List[str], length: int) -> List[str]:
    if length <= 0:
        return []
    return [w for w in words if len(w) == length]
print(find_words_of_length(["apple", "banana", "cherry", "date", "fig", "grape"], length = 5))