import os

current = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(current, file_name)

with open(full_path, 'rt') as file:
    cook_book = {}
    for line in file:
        cook = line.strip()
        count_cook = int(file.readline())
        components = []
        for count in range(count_cook):
            component, quantity, measure = file.readline().strip().split(' | ')
            components.append({'компоненты': component,
                               'количество': quantity,
                               'тип': measure
                               })
        file.readline()
        cook_book[cook] = components
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    end_components = {}
    for cook in dishes:
        for comp in cook_book[cook]:
            if comp.get('компоненты') \
                    not in end_components.keys():
                end_components[comp.get('компоненты')] = \
                    {'тип': comp.get('тип'),
                     'количество': int(comp.get('количество'))*person_count}
            else:
                end_components[comp.get('компоненты')]['количество'] +=\
                    int(comp.get('количество'))*person_count
    print(end_components)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)