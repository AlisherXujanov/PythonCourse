# FUNCTIONS 

# -------------------------- INTERMEDIATE --------------------------
# 1. Напишите логику, которая находит самую длинную строку в массиве строк.
arr = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def longest_string_max(strings):
    return max(strings, key=len)

strings = ["apple", "bananana", "cherry"]
# print(longest_string_max(strings))
# ------------------------
# ------------------------
# 2. Напишите функцию, которая принимает строку в качестве параметра и преобразует первую букву каждого слова строки в верхний регистр.      
def create_title(text:str) -> str:
    splitted_text = text.split(" ") # ["hello,", "my", "name", "is", ...]
    pool = ''
    for word in splitted_text:
        pool += word.capitalize() + " "
    return pool

text = "hello, my name is amirbek and i am a programmer"
r = create_title(text)
# print(r)
    
# ------------------------
# ------------------------
# 3. Напишите логику, которая находит самое большое число в массиве чисел.
def largest_number_max(numbers):
    return max(numbers)

numbers = [10, 20, 30, 40, 50]
# print(largest_number_max(numbers))
# ------------------------
# ------------------------
# 4. Напишите функцию, которая принимает строку в качестве параметра и подсчитывает количество гласных в строке. 
def count_vowels(text:str) -> int:
    vowels = 'aeiou'
    pool = 0
    
    for letter in text:
        if letter in vowels:
            pool += 1   
    
    return pool

r = count_vowels("hello, my name is amirbek and i am a programmer")
# print(r)

# ------------------------
# ------------------------
# 5. Создайте массив чисел. Найдите максимальное число 
# (например, 12345), затем сложите каждую цифру в числе 
# (например, 1 + 2 + 3 + 4 + 5 = 15).


def sum_all_digits(number:int) -> int:
    pool = 0
    for i in str(number):
        pool += int(i)
    return pool

number = 12345
r = sum_all_digits(number)
# print(r)

# ------------------------
# ------------------------
# -------------------------- ADVANCED --------------------------
# 1. Напишите функцию для извлечения уникальных символов или букв (которые только 1 раз указаны) из строки 
def get_uniques(text:str) -> str:
    pool = ''
    for letter in text:
        if text.count(letter) == 1:
            pool += letter
    return pool

r = get_uniques("hello, my name is amirbek and i am a programmer")
# print(r)
# ------------------------
# ------------------------
# 2. Напишите функцию для генерации строки ID (указанной длины) из случайных символов 
import random
def genere_ID(length:int) -> str:
    pool = ""

    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_upper = letters.upper()
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+'
    
    total = letters + letters_upper + numbers + symbols
    while len(pool) < length:
        pool += random.choice(total)
    return pool

print("-------------------")
r = genere_ID(10)
# print(r)
print("-------------------")
r = genere_ID(50)
# print(r)
print("-------------------")
# ------------------------
# ------------------------
# 3. Напишите функцию, которая принимает массив строк. Функция должна вернуть новый массив, в котором каждая строка перевернута. 

def reverse_each_word(arr:list[str]) -> list[str]:
    pool = []
    for word in arr:
        reversed_word = word[::-1]
        pool.append(reversed_word)
    return pool

arr = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# output: ['elppa', 'ananab', 'yrrehc', 'etad', 'yrrebredle']

r = reverse_each_word(arr)
# print(r)
# ------------------------
# ------------------------
# 4. Напишите функцию, которая принимает строку 
# слов и возвращает строку, отсортированную по длине слов. 
def sort_by_length(arr:list[str]) -> list[str]:
    # BUBBLE SORT
    sorted = False
    while not sorted:
        sorted = True
        for index in range(len(arr) - 1):
            if len(arr[index]) > len(arr[index + 1]):
                arr[index], arr[index+1] = arr[index+1], arr[index]
                sorted = False
    # return sorted(arr, key=len)

arr = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# print("Before: ", arr)
# sort_by_length(arr)
# print("After: ", arr)
# ------------------------
# ------------------------
# 5. Напишите функцию, которая принимает строку и возвращает символ, который появляется больше всего раз. 
def get_most_frequent(text:str) -> str:
    memory = text[0]
    for letter in text:
        if text.lower().count(memory) < text.lower().count(letter.lower()):
            memory = letter.lower()
    return memory

# banana = a
# cherry = r
# school = o
# This is test text = t
r = get_most_frequent("This is test text")
# print(r)
# ------------------------


