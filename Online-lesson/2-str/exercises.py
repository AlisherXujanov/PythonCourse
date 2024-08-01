# INPUT   =>   is identical to prompt() in JS
# RU:  идентичен prompt() в JS
# -----------------------------------
# GETTING STRING PARTS (==> .slice())
# '...'[start:end:step] [начало:конец:шаг]
# 'Hello'[0:2]  # He
# 'Hello'[0:5:2]  # Hlo
# 'Hello'[::2]  # Hlo
# 'Hello'[::-1] # olleH
# -----------------------------------
# INCLUDES
# len('Hello')  # 5
# "..." in "..."  => checks if the other string is 
#                    included in the string

# -----------------------------------
# REPLACE
# .replace('...', '...')  (==> .replaceAll())
# import re  # Regular Expressions
# x = "I love an Apple but sometimes I eat an orange or BANANA"
# y = ["apple", "orange", "banana"] # "apple|orange|banana"
# # [..., ..., ...].join("|")  is in JS
# y = "|".join(y)
# print("BEFORE:  => ", x)
# x = re.sub(
#     "apple|orange|banana",
#     "***",
#     x,
#     flags=re.IGNORECASE
# )
# print("AFTER:  => ", x)

# re.sub(
#     #   '...'   or    r'[^a-z]'   or    '...|...|...',  
#     #   replacement,
#     #   original_string
#     #   flags=re.IGNORECASE
# ) 
# EXAMPLES:
    # text = "Mentioning of reD, GrEen and BLUE is prohibited"
    # words_to_replace = ["red", "green", "blue"]
    # new_text = re.sub(f'{"|".join(words_to_replace)}',
    #                 "***",
    #                 text,
    #                 flags=re.IGNORECASE)
    # print(new_text)
# ----------------------------------------------------------------------------------
# name = input("What is your name? ")


# INPUT   =>   is identical to prompt() in JS
# RU:  идентичен prompt() в JS
# -----------------------------------
# GETTING STRING PARTS (==> .slice())
# '...'[start:end:step] [начало:конец:шаг]
# 'Hello'[0:2]  # He
# 'Hello'[0:5:2]  # Hlo
# 'Hello'[::2]  # Hlo
# 'Hello'[::-2] # olleH
# -----------------------------------
# INCLUDES
# len('Hello')  # 5
# "..." in "..."  => checks if the other string is 
#                    included in the string

# -----------------------------------
# REPLACE
# .replace('...', '...')  (==> .replaceAll())
# import re  # Regular Expressions
# x = "I love an Apple but sometimes I eat an orange or BANANA"
# y = ["apple", "orange", "banana"] # "apple|orange|banana"
# # [..., ..., ...].join("|")  is in JS
# y = "|".join(y)
# print("BEFORE:  => ", x)
# x = re.sub(
#     y,
#     "***",
#     x,
#     flags=re.IGNORECASE
# )
# print("AFTER:  => ", x)
# re.sub(
#     #   '...'   or    r'[a-z]'   or    '...|...|...',  
#     #   replacement,
#     #   original_string
#     #   flags=re.IGNORECASE
# ) 
# EXAMPLES:
    # text = "Mentioning of reD, GrEen and BLUE is prohibited"
    # words_to_replace = ["red", "green", "blue"]
    # new_text = re.sub(f'{"|".join(words_to_replace)}',
    #                 "***",
    #                 text,
    #                 flags=re.IGNORECASE)
    # print(new_text)
# ----------------------------------------------------------------------------------
# =========================================================
# MODIFYING STRINGS
# ОБРАБОТКА СТРОК


# CASES --------------------------------------------------- 
# Большие и маленькие буквы

# upper()           => HELLO HELLO
# capitalize()      => Hello hello
# title()           => Hello Hello

# swapcase()        => hELLO hELLO

# lower()           => hello hello
# casefold()        => hello hello
# =========================================================
# Check ---------------------------------------------------
# Проверка на соответствие

# al  == alpha == alphabetic
# num == numeric

# x = "Hello World"
# x.istitle()       # => True    является ли строка заголовком
# x.isupper()       # => False   является ли строка в верхнем регистре
# x.islower()       # => False   является ли строка в нижнем регистре
# x.isalpha()       # => False   является ли строка буквенной
# x.isalnum()       # => False   является ли строка буквенно-цифровой
# x.isdecimal()       # False    является ли строка десятичной
# x.isdigit()         # False    является ли строка цифровой
# x.isnumeric()       # False    является ли строка числовой
# x.isprintable()     # True     можно ли напечатать строку
# x.isspace()         # False    является ли строка пробелом
# x.isascii()         # True     является ли строка ASCII
#                       American Standard Code for Information Interchange
#                       Американский стандартный код для обмена информацией
# =================================================================
# find index ------------------------------------------------------
# Найти индекс

# x = "Hello World"
# x.index("o")    # 4
# x.rindex("o")   # 7

# x.find("o")     # 4
# x.rfind("o")    # 7

# x.index('z')    # ValueError: substring not found
# x.find('z')     # -1
# =================================================================
# Аlignment -------------------------------------------------------
# Выравнивание

# x = "Hello World"
# x.ljust(20, "*")    # 'Hello World********'
# x.rjust(20, "*")    # '********Hello World'
# x.center(20, "*")   # '***Hello World****'
# =================================================================
# split -----------------------------------------------------------
# Разделение строки  // Разбиение строки

# x = "This is test text \nfor hello world"
# x.split(" ")     # ['This', 'is', 'test', 'text', 'for', 'hello', 'world']
# x.rsplit(" ", 2) # ['This is test text for', 'hello', 'world']
# list(x)          # ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', ... ... ...]
# x.splitlines()   # ['This is test text ', ' for hello world']
# =================================================================
# join ------------------------------------------------------------
# Объединение строк

# fruits = ["apple", "banana", "cherry"]
# x = " ".join(fruits)  # apple banana cherry
# print(x)
# x = "-_-".join(fruits)  # apple banana cherry
# print(x)
# =================================================================
# strip -----------------------------------------------------------
# Удаление пробелов

# x = "   Hello    World   "
# x.strip()   # 'Hello    World'
# x.lstrip()  # 'Hello    World   '
# x.rstrip()  # '   Hello    World'
# =================================================================
# zfill -----------------------------------------------------------
# Добавление нулей

# x = "Hello"
# x.zfill(10)  # 00000Hello

# =================================================================
# count -----------------------------------------------------------
# Подсчет  // Считать

# x = "Hello World"
# x.count("o")  # 2
# =================================================================
# expandtabs ------------------------------------------------------
# Расширение вкладок

# "\t"  === tab
# "\n"  === new line
# x = "H\tel\tlo"
# x.expandtabs(4)  # 'H    el    lo'
# =================================================================
# format ----------------------------------------------------------
# Форматирование

# x = "Updated"
# f"This is {x} text"  # informal way of using format
# "This is {test} text".format(test=x)  # formal way of using format
# =================================================================
# startswith, endswith, in ----------------------------------------
# Начинается ли с ..., заканчивается ли на ...,  включает ли внутри ...

# x = "Hello World"
# x.startswith("Hello")  # True
# x.endswith("Hello")    # False

# "Hello" in x   # True

# x.startswith("World")  # False
# x.endswith("World")    # True