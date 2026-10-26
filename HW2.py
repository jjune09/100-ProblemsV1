words1 = [["apple", "banana"], ["apple"], ["cherry", "banana"]]

def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    print(f"ข้อมูลที่รับมา : { words}")
    word_list1 = [] #เก็บรายการข้อมูลที่ไม่ซ้ำกัน
    words_list2 = [] #เก็บข้อมูลเพื่อนับ
    count_item = 0 #นับข้อมูลที่ไม่ซ้ำกัน

    for i in words:
        for j in i:
             #print(j)
              word_list1.append(j) 
    for k in word_list1:
        if k not in words_list2:
             words_list2.append(k)
             count_item = count_item + 1
    print(f'word_list1: {word_list1}')
    print(f'words_list2: {words_list2}')
    print(f'นับข้อมูลที่ไม่ซ้ำกัน: {count_item}อย่าง')

    main_list = []
    for l in range(len(word_list1)):
         item_list = []
         for m in range(l, len(word_list1)):
                if word_list1[m] in item_list:
                   break
                else:
                     item_list.append(word_list1[m])
                if len(item_list) == count_item:
                   print(f'list ย่่ออย: {item_list}')
                   main_list.append(item_list)
    print(f'ผลลัพธื : {main_list}')
    return (count_item, main_list)
longest_unique_word_sequence(words1)
                   

