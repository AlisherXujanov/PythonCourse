# SUM  ->  sums up all the elements in the list
# RU: Суммирует все элементы в списке
# ---------------------------
# l:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = sum(l)
# print(r)
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# MAX  ->  returns the largest element in the list
# RU: Возвращает наибольший элемент в списке

# SYNTAX:  max(iterable, key=None, default=None)
#   -----------------
#   1. iterable: Required. An iterable object. ex: list, tuple, set, etc.
#           RU: Обязательный. Объект итерации. например: список, кортеж, множество и т. д.
#   -----------------
#   2. key: Optional. A function to execute to decide the order. Default is None
#           RU: Необязательный. Функция для выполнения для принятия решения о порядке. По умолчанию None
#   -----------------
#   3. default: Optional. A value to return if the iterable is empty. Default is None
#           RU: Необязательный. Значение для возврата, если итерируемый объект пуст. По умолчанию None


#   -----------------
# l = []
# r = max(l)  # ValueError: max() arg is an empty sequence
# r = max(l, default=0)  # 0
#   -----------------
# l:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = max(l)
# print(r)
#   -----------------
# words:list[str] = ['Apple', 'Banana', 'Cherry', 'Grapes', 'Elderberry']
# #                 [5,        6,        6,        6,        10]
# r = max(words, key=len)
# print(r) # Elderberry
#   -----------------
# random_numbers = [23, 11, 53, 55, 22, 14, 96]
# # GET the biggest ODD number
# def get_odd_number(num):
#     # [23, 11, 53, 55, 22, 14, 96]
#     # [23, 11, 53, 55, 0,  0,  0]
#     if num % 2 == 1:
#         return num
#     return 0

# r = max(random_numbers, key=get_odd_number)
# print(r)
#   -----------------
# words:list[str] = ['Apple', 'Bananaa', 'Cherry', 'Grapes', 'Elderberry']
# #                  [2,        4,        1,        2,        3]

# def get_len_of_vowels(word:str) -> int:
#     return len([letter for letter in word if letter.lower() in 'aeiou'])

# r = max(words, key=get_len_of_vowels) # [2, 4, 1, 2, 3]
# print(r)
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# MIN  ->  returns the smallest element in the list
# RU: Возвращает наименьший элемент в списке

# l:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = min(l)
# print(r) # 1

# ...
# EVERYTHING MIN does is similar to MAX
# RU: Все, что делает MIN, аналогично MAX
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# ========*========*========*========*========*========*========
# FILTER ->  constructs an iterator from elements of an iterable
# for which a function returns true
# RU: создает sequence из элементов листа или кортежа или текста или range-a,
# для которых функция возвращает истину
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_item(item):
#     if item % 2 == 0:
#         return True
#     return False

# r = filter(get_item, l)
# print(list(r)) # [2, 4, 6, 8, 10]
# ----------------- ----------------- ----------------- -----------------
# ----------------- ----------------- ----------------- -----------------
# words: list[str] = ['Apple', 'Bananaa', 'Cherry', 'Grapes', 'Elderberry']

# # Get words that have minumum 2 vowels inside
# # RU: Получить слова, в которых есть минимум 2 гласные буквы
# # NOTE: USE filter   ->   ИСПОЛЬЗУЙТЕ filter

# def at_least_2_vowels(word: str) -> bool:
#     vowels = [letter for letter in word if letter.lower() in 'aeiou']
#     return True if len(vowels) >= 2 else False

# result = filter(at_least_2_vowels, words)
# print(list(result))

# ----------------- ----------------- ----------------- -----------------
# ----------------- ----------------- ----------------- -----------------
