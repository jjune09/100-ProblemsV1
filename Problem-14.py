def collect_unique_words():
    unique = []
    seen = set()
    while len(unique) < 5:
        w = input("Enter a word: ").strip()
        if not w.isalpha():
            print("Only alphabetic words allowed. Try again.")
            continue
        if w not in seen:
            seen.add(w)
            unique.append(w)
        else:
            print("Duplicate — enter another word.")
    return unique
print(collect_unique_words())