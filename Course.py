# Alisher Company
#   _
#  /_|  /  *   _ /_  _  __
# /  | /_  | _) / / (- /
# --------------------------
# ------------------------------------------------------
# NOTE: IMPORTANT
# 1. Understand the task (50% solution)
# RU: Понять задачу (50% решения)
# 2. Identify the type of the last result
# RU: Определить тип конечного результата
# 3. Identify methods of current result type
# RU: Определить методы типа конечного результата
#   - it will help us to gether information
#     RU: это поможет нам собрать информацию
# 4. Think about the login (depends on the issue)
#    RU: Подумать о логике (зависит от задачи)
#    - would you need a loop        (RU: нужен ли цикл ?)
#    - would you need a condition   (RU: нужно ли условие ?)
#    - would you need a variable    (RU: нужна ли переменная ?)
# 5. Name it correctly!!!
# RU: Назовите это правильно !!!
# ------------------------------------------------------


lesson = 'Introduction'
"""
# IN Python
# ------------
# String   ("...", '...')
# triple "   =>   Multiline comment
# '''...'''   =>   Multiple comment
# "..."   =>   String (text)
# '...'   =>   String (text)

# String(123) => "123"  => in JS
# str(123)    => "123"  => in Python
# ----------------------------------------
# int()   =>   parseInt()
# type()  =>   typeof()
# ----------------------------------------
# print(int(123.5))
# print(float("123"))

# print(type("123"))      # <class 'str'>
# print(type(int("123")))  # <class 'int'>
# print(type(float("123")))  # <class 'float'>
# ----------------------------------------
# `${...}`  => String template   => JS
# f'...'   =>  Formatted string  => Python
# ----------------------------------------
# print("This is", test,  end="!!!", sep="---")
# ----------------------------------------
# test = 'Hello world'       # Global variable
# test = "Updated text"      # Update global variable
# ----------------------------------------
# x = [1, 2, 3]
# a = x[0]
# b = x[1]
# c = x[2]
# a, b, c = x
# print(a, b, c, sep="-")
# ----------------------------------------
# x = [1, 2, 3, 4, 5, 6, '...']
# first, *others, last = x
# print(first)
# print(others)
# print(last)
# ----------------------------------------
# function ...() {}
# def ...():   #  =>  def == define
# ____...

# def test():
#     global x, y
#     x = 10
#     y = 20
#     print("Hello world")  # this is inside function

# test()                # This line calls function
# print("Hello world")  # this line is out of function
# print(x)              # This line calls global variable
# -------------------------------------------------------
# x = 10
# print(x)
# del x
# print(x)

# let x = {
#     name: 'John',
# }
# delete x['name']
# -------------------------------------------------------
# input   =>  allows us to get input from user
# answer = input("How are you? ")
# print("You typed: " + answer)
# -------------------------------------------------------
# if ...:
#     ...
# elif ...:
#     ...
# else:
#     ...

"""


lesson = 'numbers'
"""
# math.ceil    => 3.33 => 4
# math.floor() => 3.33 => 3
# round()      => 3.5  => 4   => is used to round the number by 
#                               deleting the decimal part if it is 
#                               less than 5
#                       2nd param => number of digits after the decimal point
#                       RU: используется для округления числа путем 
#                           удаления десятичной части, если она меньше 5
#                       2-й параметр => количество цифр после десятичной точки
# ----------------------------------------------------------------------
# import random
# ----------------------------------------------------------------------
# random.randrange(.., ..?) # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex:  random.randrange(0, 10, step=2)  # 0, 2, 4, 6, 8
# ----------------------------------------------------------------------
# random.randint(.., ..)   # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex: random.randint(0, 10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# ----------------------------------------------------------------------
# random.random()    # gives random float number between 0 and 1
#            RU: дает случайное число с плавающей запятой между 0 и 1
# ex: round(random.random() * 100, 5)
# ----------------------------------------------------------------------

# int()       # 1
# float()     # 1.0
# complex()   # 1j

# ----------------------------------------------------------------------

# FIND PERCENTAGE
# (60 / 100) * 17  # 10.2
# 60 * 0.17        # 10.2

# ----------------------------------------------------------------------

# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	   
# %	    Modulus	        x % y	   =>    10 % 3  =>  1
# **	Exponentiation	x ** y	   =>    2 * 2 * 2 * 2   =   2**4   => 16
#! //	Floor division	x // y     =>    x // 2   => 3.5 => 3
#! -------------------------------------------------

# =	    x = 5	 x = 5	  
# +=	x += 3	 x = x + 3	
# -=	x -= 3	 x = x - 3	
# *=	x *= 3	 x = x * 3	
# /=	x /= 3	 x = x / 3	
# %=	x %= 3	 x = x % 3	
# **=	x **= 3	 x = x ** 3	
#! //=	 x //= 3	 x = x // 3	

# ----------------------------------------------------------------------

# ==	Equal	        x == y	  =>  Равно
# !=	Not equal	    x != y	  =>  Не равно
# >	    Greater than	x > y	  =>  Больше
# <	    Less than	    x < y	  =>  Меньше
# >=	Greater than or equal to	x >= y	  =>  Больше или равно
# <=	Less than or equal to	    x <= y    =>  Меньше или равно

# ----------------------------------------------------------------------

# and 	Returns True if both statements are true	    x < 5 and  x < 10	
#     RU: Возвращает True, если оба выражения истинны
# or	Returns True if one of the statements is true	x < 5 or x < 4	
#     RU: Возвращает True, если одно из выражений истинно
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10
#     RU: Инвертирует результат, возвращает False, если результат истинен

# ----------------------------------------------------------------------

# is 	    Returns True if both variables are the same object	
#       RU: Возвращает True, если обе переменные являются одним и тем же объектом
# ex:   x is y	

# is not	Returns True if both variables are not the same object	
# ex:   x is not y
#       RU: Возвращает True, если обе переменные не являются одним и тем же объектом

# ----------------------------------------------------------------------

# in 	    Returns True if a sequence with the specified value is 
#           present in the object	
#       RU: Возвращает True, если последовательность с указанным значением
#           присутствует в объекте
# ex:    x in y
	
# not in	Returns True if a sequence with the specified value is 
#           not present in the object
#       RU: Возвращает True, если последовательность с указанным значением
#           отсутствует в объекте
# ex:    x not in y


# ----------------------------------------------------------------------
#!     *args  => is used receive an arbitrary number of arguments
#  RU: используется для получения произвольного количества аргументов

# def sum(*args) -> int:
#         # This function returns sum of two numbers
#         # RU: Эта функция возвращает сумму двух чисел
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(sum(1, 2, 3, 4, 5))
# ----------------------------------------------------------------------
"""


lesson = 'if/elif/else  &&  match/case  &&  Exercises'
"""
Python has several built-in data types. Here are the most commonly used ones:

Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Text Sequence Type: str
Binary Sequence Types: bytes, bytearray, memoryview
Set Types: set, frozenset
Mapping Type: dict
Boolean Type: bool
None Type: None

# Bool   =>   bool()
# ------------------------------------------------------------------
# If / elif / else 
# if 1==2:
#     print(f'1 == 1 is => {1==2}')
# elif 1==1:
#     print(f'1 == 1 is => {1==1}')
# else:
#     print(1==2)
# ------------------------------------------------------------------
# match / case
# HTTPS_status = 200
# match HTTPS_status:
#     case 200 | 201:
#         print('OK')
#     case 404:
#         print('Not found')
#     case 301 | 302:
#         print('Redirect')
#     case _:
#         print('Unknown')
# ------------------------------------------------------------------

# EXERCISES
# 1. Reverse and input from a user    &&    Reverse a number
# RU: 
#     Берите текст от клиента и выведите на терминале. 
#     Найти зеркальное число.
# inp = input("What is your name: ")
# print(inp[::-1])
# print(str(num)[::-1])
# ----------------------------------------------------------
# 2. Swap first and last digits of a number
# RU: Поменяйте местами первую и последнюю цифры числа.
# x = 123456789
# x = str(x)
# print(int(x[-1] + x[1:-1] + x[0]))
# ----------------------------------------------------------
# 3. check if a string is a palindrome

def is_polindrome(arg) -> bool:
    if type(arg) == int:
        arg = str(arg)
    # if isinstance(arg, int):
    #     arg = str(arg)
    return arg == arg[::-1]
print(is_polindrome(input('Guess a polindrome: ')))
# ----------------------------------------------------------

# SOLUTIONS FOR PREVIOUS EXERCISES
# print(str(num)[::-1])
# print(input('Enter a number: ')[::-1])
# print(str(num)[-1] + str(num)[1:-1] + str(num)[0])
# print(str(num) == str(num)[::-1])
"""


lesson = 'strings'
"""
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
"""


lesson = 'try-except  &  Exceptions  &  Generators'
"""
# Errors in python

# 1. Compile time  
#    ex: Syntax error
# 2. Logical
#    ex: 2 + 2 == 5 ?
# 3. Run time 
#    ex: 1/0

# =========================================================================
# =========================================================================
# ERROR TYPES
# 1. SyntaxError  =>  '...  => not closed string
#     RU: не закрытая строка
#     ex: print('Hello world)

# 2. TypeError    =>  1 + '...'  =>  unsupported operand type(s) for +: 'int' and 'str'
#     RU: неподдерживаемый тип операнда (ы) для +: 'int' и 'str'
    
#     ex: print(1 + 'Hello world')

# 3. NameError    =>  x  =>  name 'x' is not defined
#     RU: имя 'x' не определено

#     ex: print(x)

# 4. IndexError   =>  [1, 2, 3][3]  =>  list index out of range
#     RU: индекс списка вне диапазона

#     ex: print([1, 2, 3][3])

# 5. ValueError   =>  int('...')  =>  invalid literal for int() with base 10: '...'
#     RU: недопустимый литерал для int() с основанием 10: '...'

#     ex: print(int('Hello world'))

# 6. KeyError     =>  {'a': 1}['b']  =>  'b' =>  not in dictionary
#     OBJECT in JS     ===     DICTIONARY in Python
#     RU: 'b' => не в словаре

#     ex: print({'a': 1}['b'])

# 7. AttributeError  =>  'Hello'.append('!')  =>  'str' object has no attribute 'append'
#     RU: объект 'str' не имеет атрибута 'append'

#     ex: print('Hello'.append('!'))
    
# 8. ZeroDivisionError  =>  1 / 0  =>  division by zero
#     RU: деление на ноль

#     ex: print(1 / 0)
    
# 9. ImportError  =>  import test  =>  No module named 'test'
#     RU: нет модуля с именем 'test'

# 10. IndentationError  =>  def func():  =>  expected an indented block
#     RU: ожидался отступный блок

#     - Forgetting to indent the code inside a function, while, for, or if statement.
#     RU: Забывая отступить код внутри функции, while, for или if оператора.

# -----------------
# usage of KEYWORD  ==>>  raise
# -----------------
# def my_fn(x:int) -> int:
#     # if not isinstance(x, int):
#     # if not x.isnumeric():
#     if type(x) != int:
#         raise TypeError('Bemiyya!!!  Nomer yoz!!!')
#         # throw new Error(...)
#     return x*x

# print(my_fn(10))

# =========================================================================
# =========================================================================
# In JavaScript
# try {}  catch {}  =>  попробуй, если получится, а если нет то перехвати ошибку

# In Python
# try: ...   except: ...  => попробуй, если получится, а если нет то пропускай ошибку

# x = 2
# z = "123"

# print("BEFORE ...")
# try:
#     print(x/z)
# except ZeroDivisionError as error:
#     print("Нельзя делить на ноль! - ", error)
# except Exception as error:
#     print("Вообще не понял - ", error)

# print("AFTER ...")
# -----------------------------------------------
# IF WE WANT TO USE MULTIPLE EXCEPTIONS

# try:
#     print(x)
# except (NameError, TypeError) as e:
#     print('Переменная не объявлена')
# -----------------------------------------------
# Block - FINALLY
# Works in any case  ->  сработает в любом случае

# try:
#     print("open file")
#     print(2/0)
# except Exception as e:
#     print(e)
# finally:
#     print("close file")

# ============================================================================
# =============================================================================
# 2==2 ? True : False  => In JavaScript
# -------------------------------------
# Ternary operator in Python
# "Yes" if condition==True else "No"
print(True) if 2==2 else print(False)

# if 2==2:
#     print('Yes')
# else:
#     print('No')
# =========================================================================
# =========================================================================

# Generators
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Create a generator for the first 10 Fibonacci numbers
fib = fibonacci(10)

# Print the Fibonacci numbers
# for num in fib:
#     print(num)

# In this example, the fibonacci function is a generator that yields 
# the first n Fibonacci numbers. We create a generator fib for the first 
# 10 Fibonacci numbers, and then we use a for loop to print each number. 
# This is more memory-efficient than creating a list of the first n 
# Fibonacci numbers, especially for large n.

"""


lesson = 'functions  &&  lambda  &&  Exercises'
"""
# def func_name(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
# func_name(1, 2, 3)
# ----------------------------------------------------------
# from typing import Union
# def func_name(arg1:Union[str, int]) -> type:
#     return arg1
# print(func_name(1))
# ----------------------------------------------------------
# default value
# ----------------------------------------------------------
# Lambda
# func_name = lambda arg1, arg2: arg1 + arg2
# print(func_name(1, 2))
# ----------------------------------------------------------
# def show_message(*children):
#     # This function needs to be finished in near future!
#     # return NotImplementedError()  =>  не было создано!
#     pass
# """


lesson = "Range && List"
"""
# range(10)              => range(0, 10)
# list(range(10))        => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10, 20)    #     => range(10, 20)
# range(10, 20, 2) #     => range(10, 20, 2)
# list(range(10, 20, 2)) => [10, 12, 14, 16, 18]
# ---------------------------------------------------------
# for (let i=0; i<10; i++) {}
# for num in range(10):
#     print(num)
#     # num = num + 1
#     num += 1
# typeof([])        =>  object
# print(type([]))   =>  <class 'list'>
# ---------------------------------------------------------
# UPDATE
# x_list[...:...] = [...]   =>  updates from ... to ... by [...]
# ---------------------------------------------------------
# ADD
# [].insert(position, element_to_add) => вставлять
# [].append()  =>  добавит элемент в конец листа
# [].extend()  =>  добавит элементы в конец листа
# ---------------------------------------------------------
# REMOVE
# "..." in x  =>  проверяет есть ли элемент в листе
# [].pop()     =>  удаляет последний элемент
# [].remove()  =>  удаляет элемент по значению
# ---------------------------------------------------------
# COPY
# [].copy() => копирует лист
# ---------------------------------------------------------
# SORT
# [].sort(reverse=True)  => меняет оригинальный лист
# sorted([])             => не меняет оригинальный лист 
#                  и можно присвоить новой переменной
# ---------------------------------------------------------
# REVERSE
# [].reverse() =>  меняет оригинальный лист
"""


lesson = "Tuples"
"""
############################ List comprehension
[ <expression> for x in <sequence> if <condition> ]
##-----------------------------------------------------
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)
# ---------------------------------------------
users = ['Aziz', 'Jomol', "Farzod", "Diana", "Laziz"]

# [x…() for … in … if … ]

z = [ name for name in users if name.endswith('z') ]
for name in users:
    if name.endswith('z'):
        z.append(name)
        
# ---------------------------------------------

# [if … else for … in … ]
a = [ name if name.endswith('z') else 'Not Found' for name in users ]
for name in users:
    if name.endswith('z'):
        a.append(name)
    else:
        a.append('Not Found')

# ---------------------------------------------
        
arr = range(100)
s = [f"Even {num}" if num%2==0 else f"Odd {num}" for num in list(arr) if num<50]
# for num in list(arr):
#     if num%2==0:
#         s.append(f"Even {num}")
#     else:
#         s.append(f"Odd {num}")
# print(s)
# ---------------------------------------------
# def double(arr):
#     return [num*2 for num in arr]
# print(double([1,2,3,4,5,6,7,8,9,10]))
# ---------------------------------------------


############################ TUPLE
# []  =>  mutable           =>  Можно изменять
# ()  =>  immutable         =>  Нельзя изменять
# ---------------------------------------------
# Tuple comprehension
# x = tuple([fruit.title() for fruit in x])
# for item in x:
#     print(item.upper())
# ---------------------------------------------
# ordered      =>  means that every item has its own index starting from 0 
#              RU: каждый элемент имеет свой индекс, начиная с 0
# unchangeable =>  means that we can not change the items after the tuple 
#                  has been created
#              RU: после создания кортежа мы не можем изменить его элементы
# Tuple Length  =>  len()

########### Двоичная система
# 0 = 0
# 1 = 1
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# 10 = 1010
# 11 = 1011
# 12 = 1100
# 13 = 1101
# 14 = 1110
# 15 = 1111
# 16 = 10000


########### Fibonacci
# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
# We have to add the last two numbers to get the next number
# RU: Мы должны добавить последние два числа, чтобы получить следующее число
# --------------------------------------------------------------------------

# Create Tuple With One Item   =>   ('...',)
# tuple()                      =>   tuple([..., ...])
# Change Tuple Values          =>   x = list(("apple", "banana", "cherry")) 

# Unpacing 
# let [x,y] = [1, 2]

# Using Asterisk*   ||    _ * _   ||   _ _ *
# a, *b, c = ("apple", "banana", "cherry")

# Multiply 
# print(("apple", "banana", "cherry") * 2)

# -------------------------------------------------------------------
# append()	Adds an element at the end of the list
# RU:      Добавляет элемент в конец списка
# clear()	Removes all the elements from the list
# RU:      Удаляет все элементы из списка
# copy()	Returns a copy of the list
# RU:      Возвращает копию списка
# count()	Returns the number of elements with the specified value
# RU:      Возвращает количество элементов с указанным значением
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# RU:      Добавляет элементы списка (или любого итерируемого объекта) в конец текущего списка
# index()	Returns the index of the first element with the specified value
# RU:      Возвращает индекс первого элемента с указанным значением
# insert()	Adds an element at the specified position
# RU:      Добавляет элемент в указанную позицию
# pop()	    Removes the element at the specified position
# RU:      Удаляет элемент в указанной позиции
# remove()	Removes the item with the specified value
# RU:      Удаляет элемент с указанным значением
# reverse()	Reverses the order of the list
# RU:      Изменяет порядок списка на обратный
# sort()	Sorts the list (changes the original)          [].sort()
# RU:      Сортирует список (изменяет оригинал)
# sorted()	Sorts the list (does not change the original)  sorted([])
# RU:      Сортирует список (не изменяет оригинал)
"""


lesson = "LOOPS"
"""
# ----------WHILE LOOP
# SYNTAXIS
# while condition == True:
#   do something
# ----------FOR LOOP
# SYNTAXIS
# for x in []:
#   print(x)
# ----------ENUMERATE
# enumerate is used to get an index for the item that we are taking from list
# ex:
#   for index, item in enumerate(list):
#       print(index, item)

# ==============================================================================
# break     => breaks up the current loop
# RU: прерывает текущий цикл
# continue  => skips the current iteration of the loop
# RU: пропускает текущую итерацию цикла
# ---------
# fruits = ["apple", "banana", "kiwi", "disgusting cherry", "mango"]
# for fruit in fruits:
#     if 'disgusting' in fruit:
#         break
#     elif 'kiwi' == fruit:
#         continue
#     else:
#         print(fruit)
# ==================================================================
# round((time.time() - start_time), 2)
# ------------
# round   => rounds the number to the specified number of digits
# RU: округляет число до указанного количества цифр
# EX: print(round(3.454, 2)) => 3.45
# ------------
# import time
# time.time() => returns the number of seconds passed since epoch
# EX: start_time = time.time()
#     end_time = time.time()
#     difference = end_time - start_time
# 
# from datetime import datetime as dt
# start_time = dt.now()
# for n in range(100):
#     print(n)
#     for n2 in range(100):
#         print(n2)

# end_time = dt.now()
# print("Execution time: ", end_time - start_time)
# ==================================================================
# for i in range(10):
    # pass
# for i in "Some text":
    # pass
# ==================================================================
# itr1 = list('abcdefghijklmnopqrstuvwxyz')
# itr2 = range(len(itr1))
# zipped = zip(itr1, itr2)

# for (item, item2) in zipped:
#     print(item, item2)
# ==================================================================
# loop with dictionaries
# for key, value in dict.items():
#     print(key, value)
# ==================================================================
# import random
# letters = "abcdefghijklmnopqrstuvwxyz"
# letters_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# numbers = "1234567890"
# symbols = "@#$%^&*"

# total_symbols_for_password = 20
# everything_included = letters + numbers + symbols

# created_password = ""
# for i in range(total_symbols_for_password):
#     random_int = random.randint(0, len(everything_included)-1)
#     created_password += everything_included[random_int]

# print(created_password)
# ==================================================================
"""


lesson = "Dictionaries  =>  словарь"
"""
# DICTIONARIES 
# Словари - это структуры данных, которые хранят данные в виде пар ключ-значение.
x = {
    "first": "Один",    "second": "Два",
    "third": "Три",     "fourth": "Четыре",
    "fifth": "Пять",    "sixth": "Шесть",
    "seventh": "Семь",  "eighth": "Восемь",
}
# print(x.get("fourth", "Не нашлось"))
# print(x["fourth"]) # => Четыре 
# print(x["www"]) # => # Error if not found
# ------------------------------------------------
# z = [ "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь" ]
# for i in z:
#     if i == "Четыре":
#         print(i)
# NOTE:
# If there are 1000 doors, when using list and seeking some of them,
# the loop we are using, opens every door one by one to check them
# But, if we use dictionary here, it directly opens the needed one.
# RU: Если есть 1000 дверей, когда мы используем <list> и ищем 
# некоторые из них, цикл, который мы используем, открывает каждую дверь
# по одной, чтобы проверить их. Но, если мы используем здесь <dict>,
# он сразу же открывает нужную.
# ------------------------------------------------
# IN JAVA-SCRIPT
# function Person(name, ..., ...) {
#     this.name = name
#     this.name = name
#     this.name = name
#     ...
# }
# let person1 = new Person(..., ..., ...)
# ------------------------------------------------
# IN PYTHON
# dict()  =>  dict(key=value, key=value, key=value)
# person = dict(name='Kamron', bemiyya=True)
# print(person)
# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}


# # ACCESSING ITEMS ---------------------------------------------------------------------------
# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default

# Object.keys(dict) => возвращает список ключей (JS)
# dict.keys()       => возвращает список ключей

# Object.values(dict) => возвращает список ключей (JS)
# dict.values()     => возвращает список значений

# Object.entries(dict) => возвращает список ключей (JS)
# dict.items()      => возвращает список кортежей (ключ, значение)

# person1 = dict(name='Javox', bemiyya='True')
# print(person1.items())


# # ADDING ITEMS -----------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# print(person1.items())
# person1['bemiyya'] = True
# person1['...'] = "..."
# person1[1] = 1
# print(person1.items())
# -----------------
# Update => updates the dict (changes the original)
# dict.update({key:value, key:value, key:value})
# person1.update({
#     "name": "Alex", 
#     "address": "Samarkand", 
#     "bemiyya":True
# })
# print(person1)
# -----------------
# If the key is not found, a new key:value pair is added to the dictionary.
# RU: Если ключ не найден, в словарь добавляется новая пара ключ: значение.

# But if it exists, then the value of the key is NOT updated.
# RU: Но если он существует, то значение ключа НЕ обновляется.
# dict.setdefault(key, value)
# person1 = dict(name='Mirsaid', bemiyya=False)
# person1.setdefault("address", "Tashkent")
# print(person1)


# # REMOVING ITEMS ---------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)

# dict.pop(key)
# del_val = person1.pop('name')
# print("del_val: ", del_val)
# print("person1: ", person1)

# res = person1.pop('www', None)
# print("Result: ", res)
# print(person1)
# dict.pop(key, default)

# dict.popitem() => removes the last inserted item
# res = person1.popitem()
# print("Result: ", res)
# print("Remaining: ", person1)

# del dict[key]
# del person1['bemiyya']
# del person1 # deletes the whole dict
# print("Remaining: ", person1)

# # MERGE ------------------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# person2 = dict(name="Covid", contageous=True)
# person3 = dict(name="Bemiyya", widespread=True)
# print("Before: ", person1)
# person1 |= person2
# print("After: ", person1)
# person1 |= person2 | person3
# print("After: ", person1)
# dict1.update(dict2)
# dict1 |= dict2
# dict1 |= dict2 | dict3 | dict4
# {**dict1, **dict2, **dict3, **dict4}
# print("Original: ", person1)
# result = {**person1, **person2, **person3}
# print("New: ", result)


# person2 = { "name2":"John",  "age2":20,  "surname2":"Khan",  "address2":"Samarkand" }
# person3 = {1:'a', 2:'b'}
# -----------------------------------
# person |= person2 | person3 
# -----------------------------------
# a = {**person, **person2, **person3 } 
# works like spread operator in JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# dict.clear()
# dict.copy()

# for key, val in person.items():
#     person[key] = ""

# p2 = person.copy()
# p2.update({"name":"Ali"})
# print(p2)
# print(person)

# person = {
#     "name": "John",
#     "age": 20,
#     "surname": "Khan",
#     "address": "Samarkand"
# }

# dict.fromkeys(iterable, value)  -> is used to create a new dictionary from the given 
#                                    sequence of elements with a value provided by the user.
# EX: 
# fruits = ['apple', 'mango', 'banana']
# result = dict.fromkeys(fruits, 0)
# print(result)
# x = dict.fromkeys(['name', 'age'], 'unknown')
# print(x)

# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# from random import randint
# def random_dict_of_github_issue_ids(stop: int, max_count: int, start: int = 0):
#     return dict.fromkeys(
#         [str(randint(start, stop)) for _ in range(randint(0, max_count))], ""
#     )
# print(random_dict_of_github_issue_ids(100, 10))
# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# zip() function
# zip(iterator1, iterator2, ...)
# Result: ...(zip object)  =>  (1, 'a'), (2, 'b'), (3, 'c')

# itr1 = list('abcdefghijklmnopqrstuvwxyz')
# itr2 = range(len(itr1))
# zipped = zip(itr1, itr2)

# for (item, item2) in zipped:
#     print(item, item2)

# # --------------------------------------------------------------------------------------------
# # DICTIONARY COMPREHENSIONs-------------------------------------------------------------------

# # Using range() function and no input list
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)


# # Lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# # Using one input list
# numdict = {x:x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# # Using two input lists
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)
"""


lesson = "Sets"
"""
# my_set = {"apple", "banana", "cherry"}
# print(my_set)

# # or use the set function and create from an iterable, e.g. list, tuple, string
# my_set_2 = set(["one", "two", "three"])
# my_set_2 = set(("one", "two", "three"))
# print(my_set_2)

# my_set_3 = set("aaabbbcccdddeeeeeffff")
# print(my_set_3)

# # careful: an empty set cannot be created with {}, as this is interpreted as dict
# # use set() instead
# a = {}
# print(type(a))
# a = set()
# print(type(a))
# # {'banana', 'apple', 'cherry'}
# # {'three', 'one', 'two'}
# # {'b', 'c', 'd', 'e', 'f', 'a'}
# # <class 'dict'>
# # <class 'set'>


# # -----------------------------------------------------------------------------------
# # NOTES  -----------------------------------------------------

# test_set = {1, 2, 3, 4, 5}
# # Don't allow duplications
# # Doesn't have order, index, keys, values, items, slices, etc...


# # 1 and True are the same and 0 and False are the same
# # 1 == True  =>  True
# # 0 == False  =>  True
# # 1 is True  =>  False
# # 0 is False  =>  False


# # -----------------------------------------------------------------------------------
# # ACCESSING ITEMS --------------------------------------------
# # loop   ||    ... in ...


# # -----------------------------------------------------------------------------------
# # ADDING -----------------------------------------------------

# # add()	                Adds an element to the set
# #   EX: x.add(4)  => changes the original set

# # update()	            Updates the set with the union of this set and others
# #  EX: x.update([4, 5, 6])  => changes the original set


# # -----------------------------------------------------------------------------------
# # Union and Intersection

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# # union() : combine elements from both sets, no duplication
# # note that this does not change the two sets
# u = odds.union(evens)
# print(u)
# # EX:
# # a = x.union(y)  # =>  x | y

# # intersection(): take elements that are in both sets
# # return a new set, that only contains the items that are present in both sets.
# i = odds.intersection(evens)  # =>  x & y
# print("intersection 1: ", i)  # =>  {}
# # EX: x.intersection(y) #  =>  x & y

# i = odds.intersection(primes)  # => {3, 5, 7}
# print("intersection 2: ", i)

# i = evens.intersection(primes)  # => {2}
# print("intersection 3: ", i)


# # -----------------------------------------------------------------------------------
# # DIFFERENCE of sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3,                   10, 11, 12}

# # difference() : returns a set with all the elements from the setA that are not in setB or in C,D... .
# # x.difference(y)     =>  x - y
# # x.difference(y, z)  =>  x - y - z

# diff_set = setA.difference(setB)
# print("difference 1: ", diff_set)

# # A.difference(B) is not the same as B.difference(A)
# diff_set = setB.difference(setA)
# print("difference 2: ", diff_set)

# # symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
# diff_set = setA.symmetric_difference(setB)
# print("difference 3: ", diff_set)

# # A.symmetric_difference(B) = B.symmetric_difference(A)
# diff_set = setB.symmetric_difference(setA)
# print("difference 4: ", diff_set)


# # -----------------------------------------------------------------------------------
# # DELETE

# # remove(x): removes x, raises a KeyError if element is not present
# my_set = {"apple", "banana", "cherry"}
# my_set.remove("apple")
# print(my_set)

# # KeyError:
# # my_set.remove("orange")

# # discard(x): removes x, does nothing if element is not present
# my_set.discard("cherry")
# my_set.discard("blueberry")
# print(my_set)

# # clear() : remove all elements
# my_set.clear()
# print(my_set)

# # pop() : return and remove a random element
# a = {True, 2, False, "hi", "hello"}
# print(a.pop())
# print(a)

# # -----------------------------------------------------------------------------------
# # Check if element is in Set
# my_set = {"apple", "banana", "cherry"}
# if "apple" in my_set:
#     print("yes")


# # -----------------------------------------------------------------------------------
# # UPDATE sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3,                    10, 11, 12}

# # update() : Update the set by adding elements from another set.
# setA.update(setB)
# print("Set update", setA)

# # Keep ONLY the Duplicates
# # intersection_update() : Update the set by keeping only the elements found in both
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.intersection_update(setB)
# print("Set intersection_update", setA)

# # difference_update() : Update the set by removing elements found in another set.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.difference_update(setB)
# print("Set difference_update", setA)

# # symmetric_difference_update():  Keeps only the elements that are NOT present in both sets.
# # Keep All, But NOT the Duplicates.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.symmetric_difference_update(setB)
# print("Set symmetric_difference_update", setA)

# Note: all update methods also work with other iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])

# # -----------------------------------------------------------------------------------
# # Copying ---------------------------------------------------------------------------
# set_org = {1, 2, 3, 4, 5}

# # this just copies the reference to the set, so be careful
# set_copy = set_org

# # now modifying the copy also affects the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)

# # use copy() to actually copy the set
# set_org = {1, 2, 3, 4, 5}
# set_copy = set_org.copy()

# # now modifying the copy does not affect the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)


# # -----------------------------------------------------------------------------------
# # Subset, Superset, and Disjoint ----------------------------------------------------
# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# # issubset(setX): Returns True if setX contains the set
# print(setA.issubset(setB))
# print(setB.issubset(setA))  # True

# # issuperset(setX): Returns True if the set contains setX
# print(setA.issuperset(setB))  # True
# print(setB.issuperset(setA))

# # isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
# setC = {7, 8, 9}
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))
# # -----------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # FROZENSET
# # Frozen set is just an immutable version of normal set.
# # While elements of a set can be modified at any time, elements of frozen set
# # remains the same after creation. Creation with: my_frozenset = frozenset(iterable)

# a = frozenset([0, 1, 2, 3, 4])

# # The following is not allowed:
# # a.add(5)
# # a.remove(1)
# # a.discard(1)
# # a.clear()

# # Also no update methods are allowed:
# # a.update([1,2,3])

# # Other set operations work
# odds = frozenset({1, 3, 5, 7, 9})
# evens = frozenset({0, 2, 4, 6, 8})
# print(odds.union(evens))
# print(odds.intersection(evens))
# print(odds.difference(evens))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# frozenset()
# frozenset({1, 3, 5, 7, 9})

"""


lesson = "Class  &&  OOP"
_1 = 'Abstract and Inheritance'
"""
# Abstract
# Inheritance

# this == self

# class User:
#     def __init__(self, name):
#         print(f"User {name} is created")
#         self.name = name

# user1 = User("John")
# print(user1)
# print(user1.name)


# __init__  => is a constructor method which is used to initialize the attributes of a class
# it is called automatically when an object is created

#############################################################################################
################ Abstraction

# "abc" here stands for abstract base class. It is first imported and then used as 
# a parent class for some class that becomes an abstract class. Its simplest implementation 
# can be done as below.


# from abc import ABC, abstractmethod
# class AbcAnimal(ABC):
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food

#     @abstractmethod
#     def get_description(self):
#         pass
#         # raise NotImplementedError


# class Pets(AbcAnimal):
#     def __init__(self, name, food, speed):
#         super().__init__(name, food)
#         self.speed = speed

#     def get_description(self):
#         return f"{self.name} eats {self.food}"


# dog = Pets("Dog", "Meat", 10)
# print(dog)
# print(dog.get_description())



# abs module is used to create abstract classes
# it is helpful when we want to create a class that will be used as a base class
# abstractmethod is used to declare abstract methods which will be implemented by the child classes
# is it used to ensure that the child classes will have the same method as the parent class
# and returns an error if the child class does not have the same method as the parent class
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.

#############################################################################################
################ Inheritence

# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# is a way of creating a new class for using details of an existing class without modifying it.
# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def test(self):
#         print("Hello world")

# class Child(Parent, ABC):
# #     Inherited members from parent class
# #     Additional members of the child class
#     def __init__(self, name, age):
#         super().__init__(name)  # => calls the parent class constructor
#         self.age = age

#     def test(self):
#         print("Hello world from child")

#     def __repr__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for debugging and logging.
#         '''
#         return f"{self.name} is {self.age} years old"

#     def __str__(self) -> str:
#         '''
#             Is used to represent the object with a string.
#             It is used for the end user.
#         '''
#         return f"{self.name} is {self.age} years old"


# child = Child("John", 20)
# print(child)
# print(child.test())
"""

_2 = 'Polymorphism and Encapsulation and Decorators'
"""
################ Polymorphism
# Polymorphism allows you define one interface and have multiple implementations.
# Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.

class Character:
    def attack(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Soldier(Character):
    def attack(self):
        return 'Soldier shoots a gun!'

class Alien(Character):
    def attack(self):
        return 'Alien uses a laser beam!'

class Robot(Character):
    def attack(self):
        return 'Robot uses a mechanical arm!'


#############################################################################################
################ Encapsulation
# is used to restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.

# class A:
    # def __init__(self):
    #     self._a = 2.  # Protected member ‘a’
    #     self.__b = 2.  # Private member ‘b’

# Real world example
class BankAccount:
    def __init__(self):
        self.__account_number = None
        self.__pin = None
        self.__balance = 0

    def set_account_details(self, account_number, pin):
        self.__account_number = account_number
        self.__pin = pin

    def get_balance(self, account_number, pin):
        if self.__account_number == account_number and self.__pin == pin:
            return self.__balance
        else:
            return "Invalid account details"

    def deposit(self, account_number, pin, amount):
        if self.__account_number == account_number and self.__pin == pin:
            self.__balance += amount
            return "Deposit successful"
        else:
            return "Invalid account details"

    def withdraw(self, account_number, pin, amount):
        if self.__account_number == account_number and self.__pin == pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return "Withdrawal successful"
            else:
                return "Insufficient balance"
        else:
            return "Invalid account details"


#############################################################################################
#################### DECORATORS

# @property   is a built-in decorator in Python that is used to define the properties
#             of an object. The @property decorator makes the work easier by
#             automatically calling the getter method when the value of the attribute is accessed.

# @classmethod is a built-in decorator in Python that is used to create class methods.
#              The class method can be called by both the class and the object.
#              This method accepts the class as the first argument that is passed automatically
#              when the method is called.

# @staticmethod is a built-in decorator in Python that defines a static method.
#               A static method doesn’t receive any reference argument whether it is called by an
#               instance of a class or by the class itself. This means that a static method can neither
#               modify object state nor class state. Static methods are restricted in what data they can
#               access - and they’re primarily a way to namespace your methods.

# -- Static method knows nothing about the class and just deals with the parameters.
# -- Class method works with the class since its parameter is always the class itself.

# Link that is about difference of two decorators:
# https://sparkbyexamples.com/python/python-difference-between-staticmethod-and-classmethod/#h-1-what-is-staticmethod


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     @staticmethod
#     def isAdult(age):
#         return age > 18

# student1 = Student('Rolf', 19)
# student2 = Student.fromBirthYear('Anna', 1990)

# print(student1.age)
# print(student2.age)


####################################################################################
####################################################################################
_3 = 'Dunder methods'

from abc import ABC, abstractmethod


class AbstractUserClass(ABC):
    name: str
    surname: str
    age: int
    email: str

    @abstractmethod
    def get_info(self):
        raise NotImplementedError(
            "This is an abstract method and needs to be implemented in the child class.")


class User(AbstractUserClass):
    def __init__(self, name: str, surname: str, age: int = 0, email: str = '') -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def __str__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'

    def __call__(self, *args, **kwargs):
        print(f"This is call fn from __call__")
        for i in args:
            print(i)
        return ''
        # ex:
        # user1("test1", "test2", "test3")  => This is call fn from __call__

    def __add__(self, other):
        return "This user has $" + str(other.budget)

    def get_info(self):
        print(f'{self.name} {self.surname}')
        return ''

    @classmethod
    def from_string(cls, string):
        if not string.count(',') == 3:
            raise Exception("String must have 4 values separated by comma.")

        # string  =>  "John, Doe, 25, test@gmail.com"
        splitted_str = string.split(",")
        name, surname, age, email = splitted_str
        # name = splitted_str[0]
        # surname = splitted_str[1]
        # age = splitted_str[2]
        # email = splitted_str[3]
        return cls(name, surname, int(age), email)

    @staticmethod
    def is_adult(age):
        return age > 18


class Client(User):
    def __init__(self, name: str, surname: str, budget: float) -> None:
        super().__init__(name, surname)
        self.budget = budget

    def __str__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def get_info(self):
        print(f'{self.name} {self.surname} has ${self.budget} budget.')
        return ''


# # =================================================
# user1 = User('John', 'Doe', 25, 'test@gmail.com')
# print(user1.get_info())
# # =================================================
# client1 = Client("Cathrine", "Mackwold", 10000)
# print(client1.get_info())
# # =================================================
# result = user1 + client1
# print(result)
# =================================================
# user1 = User.from_string("John, Doe, 25, test@gmail.com")  # classmethod
# print(user1)
# print(User.is_adult(user1.age))  # staticmethod
"""

# EXERCISES
# https://pynative.com/python-object-oriented-programming-oop-exercise/
