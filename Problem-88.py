f = open('output.txt', 'a')
num = ['m1', 'm2', 'm3', 'm4', 'm5']
for m  in num:
    f.write(f'{m}\n')
f.close()