from typing import Tuple, Set

def set_operations(set1: Set, set2: Set) -> Tuple[Set, Set]:
   
    union_set = set1 | set2          # หรือใช้ set1.union(set2)
    intersection_set = set1 & set2   # หรือใช้ set1.intersection(set2)
    return (union_set, intersection_set)

set1 = {'a', 'e', 'i', 'o', 'u'}
set2 = {'h', 'e', 'r', 'o'}
print(set_operations(set1, set2))