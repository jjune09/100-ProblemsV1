from typing import Tuple, Dict

def create_dictionary_from_tuples(tuple1: Tuple[int, ...], tuple2: Tuple[str, ...]) -> Dict[int, str]:
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have same length")
    return dict(zip(tuple1, tuple2))
print(create_dictionary_from_tuples((1, 2, 3, 4), ("ant", "cat", "dog", "cow")))
# Output: {1: 'ant', 2: 'cat', 3: 'dog', 4: 'cow'}