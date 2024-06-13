# integer  -->   int()       # 1
# float    -->   float()     # 1.0
# complex  -->   complex()   # 1j

# x = 2  # String ==  str  == text
# print(type(1j))

# import math
# x = 10.519

# ceil  ->  в вверхную сторону  (округление вверх как у потолоку)
# floor ->  в нижнюю сторону    (округление вниз как к полу)

# print("Ceil: ", math.ceil(x))
# print("Floor: ", math.floor(x))
# print("Round: ", round(x, 2))

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

# print("Randrange: ", random.randrange(10))         # 0  - 10
# print("Randrange: ", random.randrange(10, 50))     # 10 - 50
# print("Randrange: ", random.randrange(10, 50, 2))  # 10 - 50 (чётное число)
# random.randrange(.., ..?) # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex:  random.randrange(0, 10, step=2)  # 0, 2, 4, 6, 8
# ----------------------------------------------------------------------
# random.randint(.., ..)   # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# print("Randint: ", random.randint(1, 5))     # 1 - 5
# ex: random.randint(0, 10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ----------------------------------------------------------------------
# random.random()    # gives random float number between 0 and 1
#            RU: дает случайное число с плавающей запятой между 0 и 1
# ex: round(random.random() * 100, 5)
# print(random.random())  # 0 - 1  (ex:  0.425188750)
# ----------------------------------------------------------------------

# FIND PERCENTAGE
# (600000 / 100) * 17  # 102000.0
# 600000 * 0.17        # 102000.0


# ----------------------------------------------------------------------

# +	    Addition	    x + y	
# str + int = TypeError
# str + str = str
# int + int = int
# ----------------------------------
# -	    Subtraction	    x - y	
# x = 2
# # x = x - 1
# x -= 1
# print(x)
# ----------------------------------
# *	    Multiplication	x * y
# ----------------------------------
# /	    Division	    x / y
# ----------------------------------
# %	    Modulus	        x % y	   =>    10 % 3  =>  1
# Gets the reminder
# RU: Получает остаток
# 11 % 2  == 1,     15 % 4 == 3,   21 % 6 == 3
# 5 % 2  == 1,    10 % 4 == 2,   13 % 10 == 3
# ----------------------------------
# **	Exponentiation	x ** y	   =>    2 * 2 * 2 * 2   =   2**4   => 16
# 3 ** 2,    4 ** 4,  ... 
# ----------------------------------
#! //	Floor division	x // y     =>    x // 2   => 3.5 => 3
# 11 / 2  == 5.5
# 11 // 2 == 5
#! -------------------------------------------------

# =	    x = 5	 x = 5	  
# +=	x += 3	 x = x + 3	
# -=	x -= 3	 x = x - 3	
# *=	x *= 3	 x = x * 3	
# /=	x /= 3	 x = x / 3	
# %=	x %= 3	 x = x % 3	
# **=	x **= 3	 x = x ** 3	
# //=	 x //= 3	 x = x // 3	

# ----------------------------------------------------------------------
# x = 2
# print(x == 3)  # False
# print(x == 5)  # False
# print(x == 2)  # True

# print(x != 3)  # True
# print(x != 5)  # True
# print(x != 2)  # False


# ==	Equal	        x == y	  =>  Равно
# !=	Not equal	    x != y	  =>  Не равно
# >	    Greater than	x > y	  =>  Больше
# <	    Less than	    x < y	  =>  Меньше
# >=	Greater than or equal to	x >= y	  =>  Больше или равно
# <=	Less than or equal to	    x <= y    =>  Меньше или равно

# ----------------------------------------------------------------------
x = 2
# print(x == 2 and x < 5)    # True
# print(x == 2 or  x > 5)    # True
# print(x != 2 or x < 4)     # False
# print(x*2 <= 4 or x > 3)   # True
# print(x*2 <= 4 and x > 3)  # False

# print(x is 2)      # True
# print(x is not 2)  # False


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
# x = "Hello world"
# print("h" in x)      # False
# print("o" in x)      # True
# print("Amir" in x)   # False
# print("world" in x)  # True

# print("world" not in x)  # False

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
#     # This function returns sum of two numbers
#     # RU: Эта функция возвращает сумму двух чисел
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(sum(1, 2, 3, 4, 5))
# ----------------------------------------------------------------------

