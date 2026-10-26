from typing import List, Dict

def count_word_occurrences(words: List[str]) -> Dict[str, int]:
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
print(count_word_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]))