from typing import List, Dict

def create_dictionary(list1: List[int], list2: List[str]) -> Dict[int, str]:
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    return {k: v for k, v in zip(list1, list2)}
print(create_dictionary([1, 2, 3, 4], ["blue", "green", "pink", "yellow"]))
# Output: {1: 'blue', 2: 'green', 3: 'pink', 4: 'yellow'}