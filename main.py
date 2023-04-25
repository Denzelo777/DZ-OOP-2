# Задачи 1 и 2 здесь, 3 задача в отдельном файле.

from pprint import pprint

with open('cook book.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        numb_ingr = int(file.readline())
        ingredients = []
        for _ in range(numb_ingr):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
    # pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = \
                        {'measure': consist['measure'], 'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    pprint(result)


# get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])



dict_ = {}
tot_ = {}

with open('1.txt', encoding='utf-8') as f1:
    list1 = f1.readlines()
    dict_['1.txt'] = list1
    tot_[len(list1)] = '1.txt'

with open('2.txt', encoding='utf-8') as f2:
    list2 = f2.readlines()
    dict_['2.txt'] = list2
    tot_[len(list2)] = '2.txt'

with open('3.txt', encoding='utf-8') as f3:
    list3 = f3.readlines()
    dict_['3.txt'] = list3
    tot_[len(list3)] = '3.txt'

sort_ = dict(sorted(tot_.items(), key=lambda item: item[0]))

with open('result.txt', 'w', encoding='utf-8') as file:
    for key, value in sort_.items():
        res = str(value) + '\n' + str(key) + '\n' + "".join(dict_.get(value)) + '\n'
        file.write(res)