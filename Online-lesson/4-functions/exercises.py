# ------------------------ BEGINNER ------------------------
# 14. Напишите программу, которая принимает список чисел
# (например, a=[5, 10, 15, 20, 25]) и создает новый список 
# только первого и последнего элементов заданного списка.
# ------------------------------
# def first_last(arr):
#     return [arr[0], arr[-1]]


# first_last([5, 10, 15, 20, 25]) # [5, 25]
# first_last([100, 10, 15, 20])   # [100, 20]
# ==========================================================
# ==========================================================



# ------------------------ INTERMEDIATE ------------------------
# 1. Напишите функцию, которая принимает массив 
# чисел и находит второе наименьшее и второе наибольшее числа.    
def get_second_smallest_and_largest(arr:list):
    сортированный_лист = sorted(arr) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return сортированный_лист[1], сортированный_лист[-2]


massiv = [19, 22, 1, 9, 55, 12, 4]
result = get_second_smallest_and_largest(massiv)
# print(result)
# ==========================================================
# ==========================================================
# 2. Напишите функцию, которая принимает сортированный список чисел
# (список, в котором элементы сортированы от наименьшего к наибольшему)
# и другое число. Функция решает, находится ли заданное число в списке, 
# и возвращает(затем печатает) соответствующий булевый результат. 
# (Используйте бинарный поиск.)
def check_if_includes(arr:list, number:int) -> bool:
    return number in arr
    # --------------------
    # BINARY SEARCH
    # ...
# check_if_includes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)    # True
# check_if_includes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)  # Fasle
# ==========================================================
# ==========================================================
# 3. Напишите функцию, которая принимает строку в качестве параметра 
# и находит самое длинное слово в строке.
def get_longest(string: str) -> str:
    result = ''

    splitted_text = string.split(" ") # ['Hello,', 'my', 'name', 'is', 'John']
    for word in splitted_text:
        if len(word) > len(result):
            result = word

    return result


text = "Hello, my name is John"
result = get_longest(text) # "Hello"
# print(result)

# ==========================================================
# ==========================================================
# 4. Напишите функцию, которая принимает строку в качестве 
# параметра и подсчитывает количество гласных в строке.

def count_vowels(string:str) -> int:
    """Подсчитывает количество гласных в строке"""
    vowels = 'aeiou'
    result = 0
    for буква in string:
        if буква.lower() in vowels:
            result += 1
    return result

result = count_vowels("Amirbek, where are you?") # 9
# print(f"Количество гласных в строке: {result}")
# ==========================================================
# ==========================================================
# 5. Напишите функцию, которая принимает два аргумента, строку и букву, 
# и функция будет подсчитывать количество этой указанной буквы в строке.

def count_given_letter(string: str, буква: str) -> int:
    result = 0
    for letter in string:
        if буква == letter:
            result += 1
    return result


буква = "o"
result = count_given_letter("Hello, my name is John", буква) # 3
# print(f"Количество буквы {буква} в строке: {result}")
# ==========================================================
# ==========================================================
# 6. Напишите функцию, которая принимает строку и возвращает новую строку,
# в которой удалены все гласные буквы.
def delete_vowels(string:str) -> str:
    vowels = "aeiou"
    result = ""
    for буква in string:
        if буква not in vowels:
            result += буква
    return result

result = delete_vowels("Hello, my name is John") # "Hll, my nm s Jhn"
# print(result)
# ==========================================================
# ==========================================================
# 7. Напишите функцию, которая принимает строку и возвращает новую строку,
# в которой каждая гласная заменена на следующую гласную в алфавите.

def change_vowel_into_next(string:str) -> str:
    vowels = "aeiou"
    result = "H"

    for буква in string:
        if буква in vowels:
            # 1. Найти индекс буквы в строке гласных
            # 2. Если индекс последний, то взять первую букву
            # 3. Иначе взять следующую букву
            if буква != vowels[-1]:
                index = vowels.index(буква)
                result += vowels[index+1]
            else:
                result += vowels[0]
        else:
            result += буква

    return result

result = change_vowel_into_next("Hello") # "Hillu"
# print(result)


# ==========================================================
# ------------------------ ADVANCED ------------------------
# 1. Напишите функцию для извлечения уникальных символов или 
# букв (которые только 1 раз указаны) из строки

"Hello world"
# H   ello world        -> unique
# e   H llo world       -> unique
# l   He lo world       -> NOT unique
# ...
def get_uniques(text:str) -> str:
    result = ""
    current_index = 0
    for letter in text:
        before = text[0:current_index]
        after = text[current_index+1:]
        if letter not in before and letter not in after:
            result += letter
        current_index += 1
    return result

r = get_uniques("Hello world") # "He wrd"
# print("Result:", r)
# ----------------------------------------------------------
# 2. Напишите функцию для генерации строки ID (указанной длины) из случайных символов
import random
def generate_ID(length:int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alphabet.upper()
    numbers = '1234567890'

    total = alphabet + alpha_upper + numbers
    result = ''

    for i in range(length):
        random_index = random.randrange(0, len(total))
        letter = total[random_index]
        result += letter

    return result

r1 = generate_ID(10) # "aBcD1234eF"
r2 = generate_ID(5)  # "aBcD1"
# print(r1)
# print(r2)
# ----------------------------------------------------------
# 3. Напишите функцию, которая принимает строку на вход и возвращает 
# новую строку, в которой первая буква каждого слова написана с заглавной буквы. 
# Предположим, что все символы в строке - это строчные буквы и только пробелы.
pass

# ----------------------------------------------------------
# 4. Напишите функцию, которая принимает массив строк. 
# Функция должна вернуть новый массив, в котором каждая строка перевернута.
def reverse_each_string(arr:list[str]) -> list[str]:
    result = []
    for item in arr:
        result.append(item[::-1])

    return result

r = reverse_each_string(["Hello", "world"]) # ["olleH", "dlrow"]
# print(r)
# ----------------------------------------------------------
# 5. Напишите функцию, которая принимает строку слов и возвращает 
# строку, отсортированную по длине слов

def sort_by_len(text:str) -> str:
    result = []
    splitted_text = text.split(" ")  # =>  ["Hello", "my", "name", "is", "John"]
    for i in range(len(text.split(" "))):
        shortest = min(splitted_text, key=len)
        result.append(shortest)
        splitted_text.remove(shortest)
    return " ".join(result)

r = sort_by_len("Hello my name is John") # "my is name John Hello"
print(r)


# ----------------------------------------------------------
# 6. Напишите функцию, которая принимает строку и возвращает 
# символ, который появляется больше всего раз.
def find_most_frequent(string:str) -> str:
    ...


r = find_most_frequent("Hello world") # "l"
print(r)


# ----------------------------------------------------------
# 7. Напишите функцию, которая принимает строку и возвращает новую строку,
# в которой каждая гласная заменена на следующую гласную в алфавите.

vowels = "aeiou"
text = "Hello u"

def change_vowel_into_next(string:str) -> str:
    result = ""
    for letter in string:
        if letter in vowels:
            indexOfLetter = vowels.index(letter)
            if indexOfLetter == len(vowels) - 1:
                neededLetter = vowels[0]
            else:
                neededLetter = vowels[indexOfLetter + 1]
            result += neededLetter
        else:
            result += letter
    return result

result = change_vowel_into_next(text) # "Hillu"
# print(result)


