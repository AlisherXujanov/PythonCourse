# 1. Write a function to count the occurrences of each character in a string.
# RU: Напишите функцию, чтобы подсчитать количество вхождений каждого символа в строку.
def count_occurences(string): # подсчитать_вхождения
    dict = {}
    for i in string:
        dict[i] = string.count(i)
    return dict
    # return {i: string.count(i) for i in string}


# 2. Write a Python script to concatenate the following dictionaries to create a new one.
# RU: Напишите скрипт Python для объединения следующих словарей, чтобы создать новый.
def concatenate_dictionaries(*args):
    # dict = {}
    # for i in args:
    #     dict.update(i)
    # return dict
    return {key:val for dict in args for key, val in dict.items()}



# 3. Write a Python script to check whether a given key already exists in a dictionary.
# RU: Напишите скрипт Python, чтобы проверить, существует ли в словаре заданный ключ.
def check_key(dict, key):
    return key in dict


# 4. Write a Python program to iterate over dictionaries using for loops.
# RU: Напишите программу Python, чтобы перебирать словари с помощью циклов for.
def iterate_over_dict(dict):
    # for key, val in dict.items():
    #     print(key, val)
    return {print(key, val) for key, val in dict.items()}
person = {
    'name': 'John',
    'age': 26,
    'address': 'London',
}
iterate_over_dict(person)


# 5. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.
# RU: Напишите скрипт Python для печати словаря, где ключи - числа
# от 1 до 15 (оба включены), а значения - квадрат ключей.
# ex: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
def generate_dict(n):
    return {i: i*i for i in range(1, n+1)}


# 6. Write a Python program to sum all the items in a dictionary.
# RU: Напишите программу Python для суммирования всех элементов в словаре.
def sum_dict(dict):
    return sum(dict.values())

# 7. Write a Python program to multiply all the items in a dictionary.
# RU: Напишите программу Python для умножения всех элементов в словаре.
def multiply_dict(dict):
    result = 1
    for i in dict.values():
        result *= i
    return result
    # return reduce(lambda x, y: x*y, dict.values())
    
# 8. Write a Python program to remove a key from a dictionary.
# RU: Напишите программу Python для удаления ключа из словаря.
def remove_key(dc, _key):
    dc_copy = dc.copy() 
    # 1. 
    # dc_copy.pop(_key)
    # return dc_copy
    # 2.
    # del dc_copy[_key]
    # return dc_copy
    # 3. 
    return {key: val for key, val in dc_copy.items() if key is not key}

# 9. Write a Python program to sort a given dictionary by key.
# RU: Напишите программу Python для сортировки заданного словаря по ключу.
def sort_dict_by_key(dict):
    return {key: val for key, val in sorted(dict.items())}

# 10. Write a Python program to get the maximum and minimum value in a dictionary.
# RU: Напишите программу Python, чтобы получить максимальное и минимальное значение в словаре.
# ex: {'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}
def get_max_min(dict):
    return max(dict.values()), min(dict.values())


# 11. Write a Python program to remove duplicates from the dictionary.
# RU: Напишите программу Python для удаления дубликатов из словаря.
def remove_duplicates(dict):
    # Using Loop
    for key, val in dict.items():
        if dict.values().count(val) > 1:
            del dict[key]
    return dict
    # return {key: val for key, val in dict.items() if dict.values().count(val) == 1}



# 12. Write a function that takes a dict as first argument and number as second argument.
# Return a list of all the keys that have values greater than the number passed as second argument.
# RU: Напишите функцию, которая принимает словарь в качестве первого аргумента и число в 
# качестве второго аргумента. Верните список всех ключей, у которых значения больше, чем число,
# переданное в качестве второго аргумента.
# Input:   {'a': 100, 'b': 200, 'c': 300, 'd': "Hello world", 'e': True},    150
# Output:  {'b': 200, 'c': 300}
def get_keys_greater_than(dict, num):
    # return {key: val for key, val in dict.items() if val > num}
    # Using Loop
    result = {}
    for key, val in dict.items():
        if val > num:
            result[key] = val
    return result