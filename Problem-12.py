def replace_characters(som: str) -> str:
    # ทำ case-insensitive: แทนทั้งตัวพิมพ์ใหญ่และเล็ก
    mapping = {'a':'@', 'A':'@', 'l':'1', 'L':'1', 'o':'0', 'O':'0'}
    return ''.join(mapping.get(i, i) for i in som)
print(replace_characters("Hello World"))