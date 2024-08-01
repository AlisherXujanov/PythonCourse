# ================================================================
# ---------------------------- STRING ----------------------------
# ================================================================

# 1. Write a function to swap the first and last characters in a string.
# RU: Напишите функцию, чтобы поменять местами первый и последний символы в строке.
# ex:  swap_first_last("Hello") => "oellH"
def swap_first_last(string: str):   # поменять_первый_последный
    first = string[0].lower()  # 'A' -> 'a'
    last = string[-1].upper()  # 'k' -> "K"
    # [start:end:step]
    middle = string[1:-1]
    return last + middle + first


r = swap_first_last("Amirbek")  # "Kmirbea"
# print(r)
# ================================================================
# ================================================================
# 2. Write a function to remove the nth index character from a n
# onempty string.
# RU: Напишите функцию, чтобы удалить символ или букву с
# индексом n из непустой строки.


def remove_nth_index(string: str, index: int):  # удалить_с_индексом
    before = string[0:index]
    after = string[index+1:]
    return before+after


r = remove_nth_index("Amirbek", 4)  # "Amirek"
# print(r)
# ================================================================
# ================================================================
# 3. Write a function to find the second most frequent character
# in a given string.
# RU: Напишите функцию, чтобы найти второй наиболее часто
# встречающийся символ в данной строке.
# второй_наиболее_часто_встречающийся


def second_most_frequent(string):
    most_c = string[0]     # the letter that occurs most frequently
    for letter in string:
        new_count = string.count(letter)
        if new_count > string.count(most_c):
            most_c = letter
            # Hello World
            # H ------------  1 > 0
            # e ------------  1 > 1
            # l ------------  3 > 1
    string = string.replace(most_c, '')  # "Hello World" -> "elo Word"

    second_most_c = string[0]
    for letter in string:  # "elo Word"
        count = string.count(letter)
        if count > string.count(second_most_c):
            second_most_c = letter
    return second_most_c


r = second_most_frequent("Hello World")  # "o"
# print(r)
# ================================================================
# ================================================================
# 4. Write a function to convert a given string into a list of integers.
# RU: Напишите функцию, чтобы преобразовать заданную
# строку в список целых чисел.
# ex:
#   "Hello! This is 2nd task of 2024 year"
#   [2, 2, 0, 2, 4]


def convert_to_list(string: str):  # преобразовать_в_список
    numbers = []
    for letter in string:
        # "a" -> False
        # "2" -> True
        if letter.isnumeric():  # "2" - True
            numbers.append(int(letter))  # "2" => 2
    return numbers


x = "Hello! This is 2nd task of 2024 year"
r = convert_to_list(x)  # [2, 2, 0, 2, 4]
# print(r)
# ================================================================
# ================================================================
# 5. Write a function to check if a given string is a palindrome.
# RU: Напишите функцию, чтобы проверить, является ли заданная строка палиндромом.


def is_palindrome(string):  # является_палиндромом
    cleaned_string = ''.join(string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

# 12321  => polindrome
# 12345  => NOT polindrome
# madam  => polindrome
# qwert  => NOT polindrome


# ================================================================
# ================================================================
# 6. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# RU: Напишите программу на Python, чтобы получить строку, состоящую из первых 2 и последних 2 символов заданной строки.
# Если длина строки меньше 2, вместо этого верните пустую строку.
# ex: "Hello World" -> "Held"

def first_last_two(string):  # первые_2_последние_2
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]
# ================================================================
# ================================================================
# 7. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# RU: Напишите программу на Python, чтобы получить строку из заданной строки, где все вхождения ее первого символа
# были заменены на '$', кроме самого первого символа.

# INPUT:   =>  "This is test text"
# OUTPUT:  =>  "This is $es$ $ex$"

# изменить_первый_символ


def change_first_char(string, symbol: str = "$") -> str:
    if not string:
        return ""
    first_char = string[0]
    result = first_char + \
        string.lower()[1:].replace(first_char.lower(), symbol)
    return result


r = change_first_char("This is test text")  # "This is $es$ $ex$"
# print(r)

r = change_first_char("Hello World hhh HHH")  # "Hello World $$$ $$$"
# print(r)


# ================================================================================================
# ================================================================================================
# 8. Write a Python program to count and display the vowels of a given text.
# RU: Напишите программу Python, чтобы подсчитать и отобразить гласные заданного текста.
def count_vowels(string: str) -> int:  # подсчитать_гласные
    count = 0
    for letter in string:
        if letter.lower() in 'auoei':
            count += 1
    return count


r = count_vowels("Hello World")  # 3
# print(r)

# ================================================================================================
# ================================================================================================
# 9. Write a function in Python to check duplicate letters.
# It must accept a string, i.e., a sentence. The function should return
# True if the sentence has any word with duplicate letters, else return False.
# RU: Напишите функцию на Python для проверки повторяющихся букв.
# Он должен принимать строку, то есть предложение. Функция должна возвращать
# True, если в предложении есть слово с повторяющимися буквами, иначе возвращать False.
# проверить_повторяющиеся_буквы

# ex: 1. "Hello World" => True
#     2. "Python is programming language" => True
#     3. "This is test"  => False


def check_duplicate_letters(string: str) -> bool:
    for index, letter in enumerate(string):
        if index == len(string)-1:
            return False
        if letter == string[index+1]:
            return True


r = check_duplicate_letters("This is test")  # True
# print(r)
# ================================================================================================
# ================================================================================================
# 10. Write a function that takes a sentence as argument, then takes last word's first letter and
# repeats 5 times in the beginning of the sentence and at the end.
# RU: Напишите функцию, которая принимает предложение в качестве аргумента, затем берет первую букву
# последнего слова и повторяет 5 раз в начале предложения и в конце.


def repeat_first_l_of_last_word(sentence:str) -> str:
    splitted_s = sentence.split()  # ["Hello", "world"]
    last = splitted_s[-1] # "world"
    first_l = last[0]  # "w"
    return first_l*5 + sentence + first_l*5


r = repeat_first_l_of_last_word("Hello world")
# print(r)  # =>   "wwwwwHello worldwwwww"
# ================================================================================================
# ================================================================================================
# 11. Create a function that takes a text and repeats the middle
# letter three times
# RU: Создайте функцию, которая принимает текст и повторяет
# среднюю букву три раза
# Welcome   =>   Welcccome


def repeat_middle(sentence):
    length = len(sentence)
    middle_index = length // 2
    letter = sentence[middle_index] 
    return sentence[0:middle_index] + letter*3 + sentence[middle_index+1:]

r = repeat_middle("Welcome")
# print(r) # => Welcccome

r = repeat_middle("Python")
# print(r) # => Pythhhon

# ================================================================================================
# ================================================================================================
# 12. Create a function that repeats first and last half of the text n times
# RU: Создайте функцию, которая повторяет первую и вторую половину текста n раз
# "Welcome"  =>  "WelWelWelWelcomecomecomecome"

def repeat_half_n_times(sentence:str, n:int) -> str:
    length = len(sentence)
    mid = length // 2
    first_half = sentence[:mid]
    second_half = sentence[mid:]
    return first_half * n + second_half * n
    
r = repeat_half_n_times("Welcome", 4)
print(r)  # =>  "WelWelWelWelcomecomecomecome"

r = repeat_half_n_times("Welcome", 2)
print(r)  # =>  "WelWelcomecome"

r = repeat_half_n_times("Exercise", 3)
print(r)  # =>  "ExeExeExerciserciseercise"
# ================================================================================================
# ================================================================================================
# 5-from-intermediate. 
# Напишите логику, которая проверяет, содержит ли строка определенный символ.


def check_inside(sentence: str, symbol: str) -> bool:
    return symbol in sentence


r = check_inside("Hello World", "o")  # True
# print(r)

r = check_inside("Moon", "j")  # False
# print(r)
# ================================================================================================
# ================================================================================================

# 6-from-intermediate. 
# Напишите логику, которая проверяет, начинается ли строка с определённого символа.

def check_starts_with(sentence: str, symbol: str) -> bool:
    return sentence.startswith(symbol)


r = check_starts_with('Hello, world!', 'H')     # True
r = check_starts_with('Hello, world!', 'Hello')  # True
# print(r)  # True

r = check_starts_with('Hello, world!', 'h')
# print(r)  # False
# ================================================================================================
# ================================================================================================
# 3-from-advanced:
# PRIME NUMBER(Простое число) - EASIEST LEVEL
# У вас есть число между 1-20. Проверьте, простое это число или нет.
# Простое число это - всегда больше 1 и делится без остатка только на себя или на 1
# НАПРИМЕР: 2, 3, 5, 7, 13 ...
def is_prime(num: int) -> bool:
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    else:
        return True

# print(is_prime(13))  # True
# print(is_prime(7))   # True
# print(is_prime(20))  # False
# print(is_prime(25))  # False
# print(is_prime(14))  # False
# ================================================================================================
# ================================================================================================
