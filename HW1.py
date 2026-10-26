def format_strings(*args):
    print(f"ค่าที่รับเข้ามาคือ {args}")
    if len(args) == 1: 
       print('เงื่อนที่1 June')
       print(str(args[0]).replace(" ", "-").lower())
       #return str(args[0]).replace(" ", "-").upper()

    else: 
        print('เงื่อนไขที่2 ei')
        #''.join(args).replace(" ","-").upper()
        s = ''
        print(s.join(args).replace(" ","-").upper())


result = format_strings("Hello", "world", "this", "is", "a", "test")
#print(result)  # Output: "HELLOWORLDTHISISATEST"

#result = format_strings("Python", "is", "fun")
#print(result)  # Output: "PYTHONISFUN"

#result = format_strings("Hello world")
#print(result)  # Output: "HELLO-WORLD"