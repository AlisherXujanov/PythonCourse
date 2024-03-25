# 1. max()
# Return the largest item in an iterable or the largest of two or more arguments.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.

# If one item is given, it should be iterable. The largest item in the iterable is returned.
# RU: Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов.
# max(iterable, *[, key, default])

# If two or more positional arguments are provided, the largest of the positional arguments is returned.
# RU: Если предоставлено два или более позиционных аргумента, возвращается наибольший из позиционных аргументов.
# max(arg1, arg2, *args[, key])

# There are two optional keyword-only arguments.
# RU: Есть два необязательных аргумента только ключевых слов.

# key- key function where the iterables are passed and comparison is performed based on its return value
# RU: key- ключевая функция, в которой передаются итерируемые объекты,
# и сравнение выполняется на основе возвращаемого значения
# EX:
#   iterable = ['geeks', 'code', 'python', 'java']
#   max(iterable, key=len)  =>  'python'
# iterable = [30, 15, 20, 25, 30]
# print(max(iterable, key=lambda x: x%15))  # => 25
#   => here the remainder after dividing each element by
#      15 is calculated and the maximum of those values is returned
#      ex:  10%15 = 10,  15%15 = 0,  20%15 = 5,  25%15 = 10,  30%15 = 0

# The default argument specifies an object to return if the provided iterable is empty.
# If the iterable is empty and the default is not provided, a ValueErrors raised.
# EX:
#   iterable = []
#   max(iterable, default=100)  =>  100
#   max(iterable)  =>  ValueError: max() arg is an empty sequence
# ==================================
# 2. min()         Works the same way as max(), but returns the smallest value

# ===========================================================================================
# 3. map()         Returns a map object (which is an iterator) of the results after applying the
#               given function to each item of a given iterable (list, tuple etc.)
#           RU: Возвращает объект отображения (который является итератором) результатов после применения
#               заданной функции к каждому элементу заданного итерируемого объекта (список, кортеж и т. Д.)
#           EX:
#               def wordCount(n):
#                   return len(n)
#               # Or we could use:
#               # wordCount = lambda n: len(n)
#               x = map(wordCount, ('apple', 'banana', 'cherry'))
#               print(list(x))  => [5, 6, 6]
# ------------------------------------------------------------------------------
# 4. filter()      Use a filter function to exclude items in an iterable object
#           RU: Используйте функцию фильтра, чтобы исключить элементы в итерируемом объекте
#           EX:
#               def myFunc(n):
#                   # if n > 18:
#                   #     return True
#                   # else:
#                   #     return False
#                   -------------------
#                   # return True if n > 18 else False
#                   -------------------
#                   return n > 18

#               x = filter(myFunc, (5, 7, 18, 25, 32))
#               print(list(x))  =>  [25, 32]
# NOTE: The callback function should return True/False 
# depending on the value in the iterable
# RU: Функция обратного вызова должна возвращать True / False 
# в зависимости от значения в итерируемом объекте
# ------------------------------------------------------------------------------
# 5. reduce()      Use a function to reduce an iterable to a single value
#           RU: Используйте функцию для сокращения итерируемого объекта до одного значения
#           EX:
# from functools import reduce
# def myFunc(acc, next):
#     """
#         acc  - accumulator
#         next - next value
#         NOTE: the initial value of the accumulator is the first value of the iterable
#               if not given as last argument
#     """
#     return acc + next
#     # return acc if acc > next else next

# x = reduce(myFunc, (1, 2, 3, 4))
# print(x)  # =>  10

# x = map(lambda x: x*2, arr)
# print(list(x))


# def myFunc(current, next):
#     if current > next:
#         print("current > next", current)
#         return current
#     else:
#         print("current > next", next)
#         return next
# arr = [11, 22, 3, 4515, 56]
# res = reduce(myFunc, arr)
# print(res)

# ------------------------------------------------------------------------------
# 6. abs()	        Returns the absolute value of a number
#           RU: Возвращает абсолютное значение числа
#           EX:
#               x = -2   ==   abs(x) == 2
#               z = 2    ==   abs(z) == 2
#               c = complex(2)
#               print(c)
#               x = abs(c)
#               print(x)
# ------------------------------------------------------------------------------
# 7. all()	        Returns True if all items in an iterable object are true
#           RU: Возвращает True, если все элементы в итерируемом объекте истинны
#           EX:

# all()  ==  and  ==  &&
# any()  ==  or   ==  ||

# mylist = [True, 'Aziz', True, "Bemiyya"]
# x = all(mylist)  # =>  True
# print("Result", x)
# ------------------------------------------------------------------------------
# 8. any()	        Returns True if any item in an iterable object is true
#           RU: Возвращает True, если любой элемент в итерируемом объекте истинен
#           EX:
# mylist = [False, False, True]
# x = any(mylist)  # => True
# print(x)
# ------------------------------------------------------------------------------
# 9. ascii()	    Returns a readable version of an object. Replaces none-ascii characters with escape character
#       American Standard Code for Information Interchange
#           RU: Возвращает читаемую версию объекта. Заменяет символы, не являющиеся ASCII-символами, символом экранирования
#               ASCII - американский стандартный код для обмена информацией
# #           EX:
# x = ascii("My name is Ståle")  # => 'My name is St\xe5le'
# print(x)

# ------------------------------------------------------------------------------
"""
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
"""
# 10. bin()	        Returns the binary version of a number
#           RU: Возвращает двоичную версию числа
#           EX:
#               x = bin(36)  =>  0b100100
# vice versa is =>  int(0b100100)  =>  36

# To get a binary (10101010) version of letters we can use: 
#  ord('A')  =>  65
#  bin(ord('A'))   =>  0b1000001

# ------------------------------------------------------------------------------
# 11. bool()	    Returns the boolean value of the specified object
#               Anything that is not empty, or 0, or None is True
#           RU: Возвращает логическое значение указанного объекта
#               Любое значение, которое не является пустым, или 0, или None, является True
#           EX:

#               x = bool(5) => True,     x = bool(0) => False,   ...
# ------------------------------------------------------------------------------
# 12. complex()	    Returns a complex number (x+yj) or converts a string or number to a complex number
#           RU: Возвращает комплексное число (x + yj) или преобразует строку или число в комплексное число
#           EX:
#               x = complex(3, 5)  =>  (3+5j)
# ------------------------------------------------------------------------------
# 13. dict()	    Returns a dictionary (Array)
#           RU: Возвращает словарь (массив)
#           EX:
# x = dict(name = 'John', age = 36, country = 'Norway')
# ------------------------------------------------------------------------------
# 14. dir()	        Returns a list of the specified object's properties and methods
#           RU: Возвращает список свойств и методов указанного объекта
#           EX:
# x = dir(bool)
# print(x)
# [print(z) for z in x]
# ------------------------------------------------------------------------------
# 15. enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
#           RU: Принимает коллекцию (например, кортеж) и возвращает ее в виде объекта перечисления
#           EX:
# x = ['apple', 'banana', 'cherry']
# y = enumerate(x)
# print(list(y))  # =>  [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# for (index, value) in enumerate(x):
#     print(f'{index} => {value}')

# ------------------------------------------------------------------------------
# 16. float()	    Returns a floating point number
# print(float(2)) # => 2.0
# ------------------------------------------------------------------------------
# 17. help()	    Executes the built-in help system
#           RU: Выполняет встроенную систему справки
#           EX:
#               print(help('modules'))
#               print(help('print'))
#               ...

# ------------------------------------------------------------------------------
# 18. id()	        Returns the id of an object
#           RU: Возвращает идентификатор объекта
#           EX:
# x = ('apple', 'banana', 'cherry')
# print(id(x))  # =>  140714640543488
# print(id(list))
# ------------------------------------------------------------------------------
# 19. input()	    Allowing user input
# ------------------------------------------------------------------------------
# 20. int()	        Returns an integer number
# ------------------------------------------------------------------------------
# 21. isinstance()	Returns True if a specified object is an instance of a specified object
#           RU: Возвращает True, если указанный объект является экземпляром указанного объекта
#           EX:
#               print(isinstance(5, int))  # True
#               print(isinstance(5, str))  # False
#               print(type(5) == int)  # True
#               print(type(5) == str)  # False
# is almost similar as type(...)
# RU: почти похоже как type (...)
# ------------------------------------------------------------------------------
# 22. len()	        Returns the length of an object
# ------------------------------------------------------------------------------
# 23. list()	    Returns a list
# ------------------------------------------------------------------------------
# 24. open()	    Opens a file and returns a file object
# ------------------------------------------------------------------------------
# 25. pow()	        Returns the value of x to the power of y
# pow(3, 4) # 81   ==>   3 ** 4    ==>   3 * 3 * 3 * 3
# 2 ** 2  # 2^2  ==  4
# pow(2, 2)  # 2^2  ==  4
# ------------------------------------------------------------------------------
# 26. print()	    Prints to the standard output device
# ------------------------------------------------------------------------------
# 27. range()	    Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# ------------------------------------------------------------------------------
# 28. set()	        Returns a new set object
# ------------------------------------------------------------------------------
# 29. str()	        Returns a string object
# ------------------------------------------------------------------------------
# 30. sum()	        Sums the items of an iterator
# ------------------------------------------------------------------------------
# 31. tuple()	    Returns a tuple
# ------------------------------------------------------------------------------
# 32. type()	    Returns the type of an object
# ------------------------------------------------------------------------------
# 33. zip()	        Returns an iterator, from two or more iterators
#           RU: Возвращает итератор из двух или более итераторов
#           EX:
#               x = zip(['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple'])
#               print(next(x))  =>  ('apple', 'orange')
# fruits = ['apple', 'banana', 'cherry', 'orange', 'lemon', 'pineapple']
# cars = ['BMW', 'Volvo', 'Ford', 'Mazda']
# z = zip(fruits, cars)
# for (fruit, car) in z:
#     print(fruit, car)

# x = [1, 2, 3, 4, 5]
# z = ['a', 'b', 'c']

# for num, letter in zip(x, z):
#     print(num, letter)


#! for more info visit sites:
# * 1. Programmiz  =  https://www.programiz.com/python-programming/methods/built-in
# * 2. w3schools   =  https://www.w3schools.com/python/python_ref_functions.asp
# * 3. python.org  =  https://docs.python.org/3/library/functions.html
