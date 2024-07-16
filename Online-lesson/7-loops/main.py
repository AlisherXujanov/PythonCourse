fruits = ["apple", "banana", "mango", "orange",
          "papaya", "pear", "pine"]

# -----------------------------------
# for idx, fruit in enumerate(fruits):
#     print(idx, fruit)
# -----------------------------------
# counter = 0
# for i in range(100):
#     counter += 1
# print(counter)
# -----------------------------------
# counter = 0
# for i in range(100):   # 100 == 100
#     counter += 1
#     for i2 in range(100):  # 100 x 100  == 10000
#         ...
# print(counter)
# -----------------------------------
# import time

# counter = 0
# start = time.time()
# for i in range(1000):   # 1000 == 1000
#     for i2 in range(1000):  # 1000 x 1000  == 1000000
#         counter += 1
# end = time.time()

# total = end - start
# print(counter)
# print("Total time: ", total)
# -----------------------------------
# def sumUpN(number:int) -> int:
#     pool = 0
#     for i in range(number):  # 0-99
#         pool += i
#     return pool
# # 1+2+3+4+5+...+99   =>  4950
# result = sumUpN(100)
# print(result)
# -----------------------------------
# counter = 0
# while counter < 10:
#     counter += 1
#     print("*" * counter)
# -----------------------------------
# counter = 10
# while counter > 0:
#     counter -= 1
#     print("*" * counter)
# -----------------------------------
# counter = 0
# while counter < 10:
#     counter += 1
#     needed_spaces = " " * (10 - counter)
#     print(needed_spaces + "*" * counter)
#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********
# **********
# -----------------------------------
# counter = 0
# while counter < 5:
#     counter += 1
#     needed_spaces = " " * (5 - counter)
#     print(needed_spaces + "* " * counter)
# #          *
# #         * *
# #        * * *
# #       * * * *
# #      * * * * *


# ===================================================
# break         =>  exit from the loop         (STOP == СТОП)
# continue      =>  skip the current iteration (SKIP == ПРОПУСТИТЬ)
# counter = 0
# while counter < 10:
#     counter += 1
#     if counter % 2 == 0  and counter != 8:
#         continue
#     elif counter == 8:
#         break
#     print(counter)


# ===================================================
# ===================================================
# HOMEWORK
# ----------------------
# 1. Create piramid
#     *
#    ***
#   *****
#  *******
# *********
# ----------------------
# 2. Guess a number
#     - Generate a random number between 1 and 100
#     - Ask user to guess a number
#     - If user guessed the number, print "Congratulations"
#     - If user didn't guess the number, print "Try again"
# RU:
#     - Сгенерировать случайное число от 1 до 100
#     - Попросить пользователя угадать число
#     - Если пользователь угадал число
#         - Вывести "Поздравляю"
#     - Если пользователь не угадал число
#         - Вывести "Попробуйте еще"
# ----------------------