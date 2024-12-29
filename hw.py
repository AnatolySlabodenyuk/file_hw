import os

# Задание 1
cook_book_file_path = 'recipes.txt'
full_path = os.path.join(os.getcwd(), cook_book_file_path)

cook_book = {}

with open(full_path, encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()

        ingredient_count = int(file.readline().strip())

        ingredient_data_list = []
        for _ in range(ingredient_count):
            ingredient_data = (file.readline().strip()).split(' | ')
            ingredient_data_list.append(
                {
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                }
            )

            cook_book[dish_name] = ingredient_data_list

        file.readline()


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for dish in dishes:
        for cook_book_dish in cook_book[dish]:
            result_dict[cook_book_dish['ingredient_name']] = {
                'measure': cook_book_dish['measure'],
                'quantity': cook_book_dish['quantity'] * person_count
            }

    return result_dict


# Задание 3
path_to_sorted_files = 'sorted'
full_path_to_sorted_files = os.path.join(os.getcwd(), path_to_sorted_files)

path_list = os.listdir(full_path_to_sorted_files)
file_data = []

for path_to_file in path_list:
    with open(os.path.join(full_path_to_sorted_files, path_to_file), encoding='utf-8') as sorted_file:
        lines = sorted_file.readlines()
        file_data.append((len(lines), lines, path_to_file))

file_data.sort(key=lambda x: x[0])

path_to_result_file = 'result.txt'
full_path_to_result_file = os.path.join(os.getcwd(), path_to_result_file)

with open(full_path_to_result_file, 'w', encoding='utf-8') as result_file:
    for data in file_data:
        result_file.write(
            f'{data[2]}\n'
            f'{data[0]}\n'
            f'{''.join(data[1])}\n'
        )
