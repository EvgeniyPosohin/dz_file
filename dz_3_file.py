import os

list_file = ['1.txt', '2.txt', '3.txt']
list_read = []
name_txt = {}
for i in range(len(list_file)):
    full_path = os.path.join(os.getcwd(), list_file[i])
    with open(full_path, 'r', encoding='utf-8') as file:
        list_read.append(file.readlines())
        name_txt[len(list_read[i])] = list_file[i]
list_read.sort()
list_read.reverse()
print(list_read)
print(name_txt)
with open('dz_3.txt', 'w') as file:
    for id, i in enumerate(sorted(name_txt)):
        file.write(name_txt[i]+'\n')
        file.write(str(i)+'\n')
        file.write(''.join(list_read[id])+'\n')







