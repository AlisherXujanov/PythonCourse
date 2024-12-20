# 1. Write a function to count the occurrences of each character in a string.
# RU: Напишите функцию для подсчета вхождений каждого символа в строке.
def count_occurences(string):  # подсчитать_вхождения
    ...


count_occurences("abaaa")
# {'a': 4,  "b": 1}


# =================================================================================
# =================================================================================
# 2. Write a Python script to concatenate the following dictionaries to create a new one.
# RU: Напишите скрипт Python для объединения следующих словарей для создания нового.

def concatenate_dictionaries(*args) -> dict:
    ...


x = {'a': 1, 'b': 2}
x2 = {'c': 3, 'd': 4}
x3 = {'e': 5, 'f': 6}
x4 = {'g': 7, 'h': 8}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
concatenate_dictionaries(x, x2, x3, x4)

# =================================================================================
# =================================================================================
# 3. Write a Python script to check whether a given key already exists in a dictionary.
# RU: Напишите скрипт Python для проверки, существует ли данный ключ уже в словаре.


def check_key(dict, key):
    ...


check_key({"a": 1, "b": 2}, "a")  # True
# =================================================================================
# =================================================================================
# 4. Write a Python program to iterate over dictionaries using for loops.
# RU: Напишите программу Python для итерации по словарям с помощью циклов for.


def iterate_over_dict(dict):
    ...


iterate_over_dict({
    'name': 'John',
    'age': 26,
    'address': 'London',
})
# name: John
# age: 26
# address: London
# =================================================================================
# =================================================================================
# 5. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.
# RU: Напишите скрипт Python для печати словаря, где ключи - числа
# от 1 до n (оба включены), а значения - квадрат ключей.
# ex: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def generate_dict(n):
    ...


generate_dict(5)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# =================================================================================
# =================================================================================
# 6. Write a Python program to sum all the items in a dictionary.
# !!! NOTE: values could be int or str, if str, convert to int
# But, if the value is not convertible to int, skip it.
# ----------------
# RU: Напишите программу Python для суммирования всех элементов в словаре.
# !!! ПРИМЕЧАНИЕ: значения могут быть int или str, если str, преобразуйте в int
# Но, если значение нельзя преобразовать в int, пропустите его.
# ----------------
# ex:  x =  {...: "10", ...: 'qwe', ...: 5}  => 15
# ----------------
def sum_dict(dict):
    ...


sum_dict({
    'a': 1,
    'b': "2",
    'c': "abc",
    'd': 4,
})

# =================================================================================
# =================================================================================
# 7. Write a Python program to multiply all the items in a dictionary.
# !!! NOTE: values could be int or str, if str, convert to int
# But, if the value is not convertible to int, skip it.
# ----------------
# RU: Напишите программу Python для умножения всех элементов в словаре.
# !!! ПРИМЕЧАНИЕ: значения могут быть int или str, если str, преобразуйте в int
# Но, если значение нельзя преобразовать в int, пропустите его.
# ----------------
# {...: "10", ...: 'qwe', ...: 5}  => 50


def multiply_dict(dict):
    ...


multiply_dict({
    'a': 1,
    'b': 3,
    'c': 2,
    'd': 4,
})
# 24
# =================================================================================
# =================================================================================
# 8. Write a Python program to remove a key from a dictionary.
# RU: Напишите программу Python для удаления ключа из словаря.


def remove_key(dc, _key):
    ...


remove_key({
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}, 'b')
# {'a': 1, 'c': 3, 'd': 4}

# =================================================================================
# =================================================================================

# 9. Write a Python program to sort a given dictionary by key.
# RU: Напишите программу Python для сортировки заданного словаря по ключу.
# ------------
# ex: {5:"a",  7:"c",   2:"b"} => {2:"b",   5:"a",   7:"c"}
# ------------


def sort_dict_by_key(dict):
    ...


sort_dict_by_key({
    5: "a",
    7: "c",
    2: "b",
})
# {2: 'b', 5: 'a', 7: 'c'}
# =================================================================================
# =================================================================================
# 10. Write a Python program to get the maximum and minimum value in a dictionary.
# RU: Напишите программу Python для получения максимального и минимального значения в словаре.
# ------------
# ex: {'x':500, 'y':5874, 'z': 560, 'a': 7, 'b': 35, 'c': 113}
# ------------


def get_max_min(dict):
    ...


get_max_min({
    'x': 500,
    'y': 5874,
    'z': 560,
    'a': 7,
    'b': 35,
    'c': 113,
})
# 5874, 7
# =================================================================================
# =================================================================================

# 11. Write a Python program to remove duplicates from the dictionary.
# First, leave at least one item from duplicates
# Second, delete all duplicates
# RU: Напишите программу Python для удаления дубликатов из словаря.
# Во-первых, оставьте хотя бы один элемент из дубликатов
# Во-вторых, удалите все дубликаты


def remove_duplicates(dict):
    # Using Loop
    for key, val in dict.items():
        if dict.values().count(val) > 1:
            del dict[key]
    return dict
    # =================================
    # return {key: val for key, val in dict.items() if dict.values().count(val) == 1}
    # =================================
    # total = {}
    # for key, value in dict.items():
    #     if value not in total.values():
    #         total[key] = value
    # return total


# ex: {'x':1, 'y':2, 'z':2, 'a':3, 'b':1, 'c':3}
# =>  {x':1, 'y':2, 'a':3}

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


# =============================================================================
# =============================================================================

# 14. Write a function that takes a dictionary as an argument and returns
# a new dictionary with the keys and values reversed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента
# и возвращает новый словарь с обратными ключами и значениями.
def reverse_dict(d):
    return {value: key for key, value in d.items()}


# =============================================================================
# =============================================================================
# 15. Write a function that takes a list of dictionaries as an argument
# and returns a sum of numeric values of all dicts
# RU: Напишите функцию, которая принимает список словарей в качестве аргумента
# и возвращает сумму числовых значений всех словарей
x = {'a': 1, 'b': "2", "c": "Hello"}
z = {'d': "4", 'e': 3, "f": "World"}
a = {'g': 5, 'h': "!!!", "i": "6"}
arr = [x, z, a]
# test(arr)  #  21


def sum_numeric_values(arr_of_dicts: list[dict]) -> int:
    total = 0
    for dict in arr_of_dicts:
        for val in dict.values():
            if str(val).isnumeric():
                total += int(val)
    return total

# =============================================================================
# =============================================================================
# 16. Write a function that takes a dictionary as an argument and returns a new
# dictionary that contains only the key-value pairs where the value is a string.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента и возвращает
# новый словарь, который содержит только пары ключ-значение, где значение - строка.


# =============================================================================
# =============================================================================

# 17. Write a function that takes a dictionary as an argument and
# returns a new dictionary that contains only the key-value pairs where the key is a string.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента и
# возвращает новый словарь, который содержит только пары ключ-значение, где ключ - строка.
def string_vals_of_dict(d: dict) -> dict:
    result = {}
    for key, val in d.items():
        if type(val) == str and not val.isnumeric():
            result[key] = val
    return result

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


# 18. Write a function that takes two dictionaries as arguments and returns a
# new dictionary that contains only the key-value pairs that are common to both dictionaries.
# RU: Напишите функцию, которая принимает два словаря в качестве аргументов и
# возвращает новый словарь, который содержит только пары ключ-значение, которые
# присутствуют в обоих словарях.
a = {'a': 1, 'b': 2, 'c': 3}
b = {'a': 1, 'b': 2, 'd': 4}
result = {'a': 1, 'b': 2}


def del_identical_pairs(dict1, dict2) -> dict:
    total = {}
    for key1, val1 in dict1.items():
        for key2, val2 in dict2.items():
            if key1 == key2 and val1 == val2:
                total[key1] = val1
    return total

# =============================================================================
# =============================================================================
# 19. Write a function that takes two dictionaries as arguments and returns a new dictionary that contains the key-value pairs from the first dictionary that are not in the second dictionary.
# RU: Напишите функцию, которая принимает два словаря в качестве аргументов и возвращает новый словарь, который содержит пары ключ-значение из первого словаря, которых нет во втором словаре.


def get_not_identicals(dict1: dict, dict2: dict) -> dict:
    total = {}
    for key, val in dict1.items():
        if key not in dict2.keys():
            total[key] = val
    return total


# =============================================================================
# =============================================================================
# 20. Write a function that takes a dictionary as an argument and returns
# a new dictionary that contains the same key-value pairs as the original
# dictionary, but with any duplicate values removed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента и
# возвращает новый словарь, который содержит те же пары ключ-значение, что
# и исходный словарь, но с удаленными дубликатами значений.

def del_identical_vals(dict):
    dict_set = []
    for i in dict.values():
        if i not in dict_set:
            dict_set.append(i)

    total = {}
    for key, val in dict.items():
        if val in dict_set and val not in total.values():
            total[key] = val
    return total


test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 3, 'f': 4}


# =============================================================================
# =============================================================================

# 21. Write a function that takes a dictionary as an argument and returns a new dictionary that contains the same key-value pairs as the original dictionary, but with any keys that contain the letter 'a' removed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента и возвращает новый словарь, который содержит те же пары ключ-значение, что и исходный словарь, но с удаленными ключами, содержащими букву 'a'.


def del_keys_with_a(dict):
    return {key: val for key, val in dict.items() if 'a' not in key}


# =============================================================================
# =============================================================================
# 22. Write a function that takes a dictionary as an argument and returns a new dictionary that contains the same key-value pairs as the original dictionary, but with any values that contain the letter 'a' removed.
def del_vals_with_a(dict):
    return {key: val for key, val in dict.items() if 'a' not in val}
