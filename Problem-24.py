from typing import List, Tuple, Dict

def store_student_nicknames(data: List[Tuple[str, str]]) -> Dict[str, str]:
    # data is list of (student_id, nickname)
    return {sid: nick for sid, nick in data}
print(store_student_nicknames([("123456", "Alice" ), ("654321", "Bob"), ("112233", "Charlie")]))
# Output: {'123456': 'Alice', '654321': 'Bob', '112233': 'Charlie'}