def print_rectangle_pattern(rows: int, columns: int) -> None:
    """
    พิมพ์รูปสี่เหลี่ยม rows x columns ด้วยเครื่องหมาย '*'
    """
    for _ in range(rows):
        print('*' * columns)

print_rectangle_pattern(5, 5)