from typing import List

def calculate_required_grades(current_gpa: float, target_gpa: float, credits: List[int]) -> List[str]:
    # กำหนดค่าเกรดและคะแนนที่สอดคล้อง
    grade_scale = {
        4.0: "A",
        3.5: "B+",
        3.0: "B",
        2.5: "C+",
        2.0: "C",
        1.5: "D+",
        1.0: "D"
    }
    # คำนวณเกรดเฉลี่ยรวมที่ต้องการทั้งหมด
    total_credits = sum(credits)

    # คำนวณผลรวมคะแนนรวมที่ต้องการ (target GPA * หน่วยกิตรวม)
    required_total_points = target_gpa * total_credits

    # สมมติว่าผลลัพธ์ต้องเฉลี่ยในแต่ละวิชาเท่ากัน
    avg_required_point = required_total_points / total_credits

    # หาค่าเกรดตัวอักษรที่ใกล้เคียงและสูงพอให้ถึง target GPA
    closest_grade = "D"
    for point, letter in sorted(grade_scale.items(), reverse=True):
        if avg_required_point <= point:
            closest_grade = letter

    # คืนค่าเกรดทั้ง 5 วิชาเป็นตัวเดียวกัน
    return [closest_grade] * 5
print(calculate_required_grades(2.8, 3.2, [3, 4, 3, 2, 3]))