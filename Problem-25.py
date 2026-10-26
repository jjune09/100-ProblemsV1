from typing import List, Tuple, Dict

def store_student_scores(student_data: List[Tuple[str, str, float]]) -> Dict[str, Dict[str, float]]:
    result = {}
    for sid, name, score in student_data:
        result[sid] = {"name": name, "score": float(score)}
    return result 
print(store_student_scores([
("123456", "Alice", 85.5),
("654321", "Bob", 92.0),
("112233", "Charlie", 78.0)
]))
