import os

list_file = ['1.txt', '2.txt', '3.txt']
name_txt = {}
for i in range(len(list_file)):
    full_path = os.path.join(os.getcwd(), list_file[i])
    with open(full_path, 'r', encoding='utf-8') as file:
        x = file.readlines()
        name_txt[len(x)] = [list_file[i], x]
print(sorted(name_txt))

with open('dz_3.txt', 'w') as file:
    for i in sorted(name_txt):
        file.write(name_txt[i][0]+'\n')
        file.write(str(i)+'\n')
        file.write(''.join(name_txt[i][1])+'\n')







