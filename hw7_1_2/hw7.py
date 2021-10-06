from pprint import pprint

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                ingredient_name_, quantity_, measure_ = file.readline().split('|')
                temp_list.append(
                    {'ingredient_name': ingredient_name_, 'quantity': int(quantity_), 'measure': measure_.strip()}
                )
            cook_book[dish_name] = temp_list
            file.readline()

    return cook_book

pprint(get_cook_book('recipes.txt'))

def get_shop_list_by_dishes(dishes, person_count, cook_book=get_cook_book('recipes.txt')):
    new_cook_book = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient_name in cook_book[dish]:
                if ingredient_name['ingredient_name'] not in new_cook_book:
                    spec = {'measure': ingredient_name['measure'], 'quantity': int(ingredient_name['quantity']) * person_count}
                    new_cook_book[ingredient_name['ingredient_name']] = spec
                else:
                    new_cook_book[ingredient_name['ingredient_name']]['quantity'] += int(ingredient_name['quantity']) * person_count

    return new_cook_book

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))