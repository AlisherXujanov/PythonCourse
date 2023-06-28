# 1. Find an average number of given numbers of the list 
# and return nearest integer from given list
# RU: Найти среднее число данного списка и вернуть ближайшее 
# целое число из данного списка.
# INPUT:  [1, 10, 40, 35, 20, 30, 50, 60, 70]
# OUTPUT: 37.777...  =>  35  =>  index-3
def nearest_average(arr):
    average = round(sum(arr) / len(arr))
    # return min(arr, key=lambda x: abs(x - average))
    # ---------------------------
    # Using loop
    nearest_value = arr[0]
    for el in arr:
        if abs(el - average) < abs(nearest_value - average):
            nearest_value = el
    return nearest_value


# print(nearest_average([1, 10, 40, 34, 20, 30, 50, 60, 70]))


# =========================================================================
# 2. Print stars (*) in the shape of a pyramid with N number of steps.
# pyramid(4) =>
#    *
#   ***
#  *****
# *******
def pyramid(n):
    for i in range(n):
        print(' '*(n-i-1)   +   '*'*(i * 2 + 1))


# =========================================================================
# 3. Write a Python program to find those numbers which are 
# divisible by 7 and multiples of 5, between 1500 and 2700 
# (both included).
# RU: Напишите программу на Python для поиска тех чисел, 
# которые делятся на 7 и кратны 5, в диапазоне от 1500 до 2700 
# (включительно).

# 7 and 5 
# 1500 and 2700
def find_numbers():
    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 == 0:
            print(i)

# ===========================================================================
# 4. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong 
# then the prompt appears again until the guess is correct, on successful 
# guess, user will get a "Well guessed!" message, and the program will exit.
# ---------------------------------------------------------------
# RU: Напишите программу на Python, чтобы угадать число от 1 до 9.
# Примечание: пользователю предлагается ввести догадку. Если пользователь
# угадывает неправильно, то подсказка появляется снова, пока догадка не будет
# правильной, при успешном угадывании пользователь получит сообщение «Хорошо
# угадано!» и программа выйдет.
import random
def guess_number():
    rand = random.randint(1, 9)
    num = int(input("Enter a number between 1 and 9: "))
    lives = 3
    while rand != num and lives > 0:
        lives -= 1
        print(f"You have {lives} lives left!")
        num = int(input("You guessed wrong. Try again: "))
    print("Well guessed!")

# guess_number()
# ===========================================================================
# 5. Write a Python program to construct the following pattern, 
# using a nested for loop.
# RU: Напишите программу на Python для построения следующего узора,
# используя вложенный цикл for.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
def pattern(n):
    for i in range(n):
        print('*' * i)
    for i in range(n, 0, -1):
        print('*' * i)

pattern(5)
    
# ===========================================================================
# 6. Write a program that takes a range of 100 numbers 
# and checks if the number is dividible to 3, 5 or both.
# Then takes these numbers and sums them all together
# ----------------------------------------------------
# RU: Программа принимает диапазон 100 чисел и проверяет,
# делится ли число на 3, 5 или на оба. Затем возмите эти числа
# и суммируйте их всех вместе и скажите какое число ЧЁТНОЕ ИЛИ НЕТ.
def сумма_кратных_чисел():
    сумма_кратных = 0
    for число in range(100):
        if число % 3 == 0 or число % 5 == 0:
            print(число)
            сумма_кратных += число
    print("Сумма кратных чисел равна: " + str(сумма_кратных))

сумма_кратных_чисел()
# ===========================================================================

# 7. Write a program that prints out the first 100 prime numbers.
# RU: Напишите программу, которая выводит первые 100 простых чисел.
tub_sonlar = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
def n_prime_numbers(n):
    """Эта функция принимает целое число n в качестве входных данных и возвращает список первых n простых чисел"""
    простые_числа = []
    текущее_число = 2
    while len(простые_числа) < n:
        является_простым = True
        for делитель in range(2, текущее_число):
            if текущее_число % делитель == 0:
                является_простым = False
                break
        if является_простым:
            простые_числа.append(текущее_число)
        текущее_число += 1
    return простые_числа

n_prime_numbers(10)
# RU: Код выше - определяет функцию с именем n_prime_numbers, которая
# принимает целое число n в качестве входных данных и возвращает список первых n простых чисел.
# Функция использует цикл while для генерации простых чисел, начиная с первого простого числа 2.
# Внутри цикла while код проверяет, является ли текущее число простым, перебирая все целые числа
# от 2 до текущего числа - 1. Если текущее число делится на любое из этих чисел, то оно не является
# простым, и код устанавливает логический флаг is_prime в False. Если текущее число не делится на
# любое из этих чисел, то оно является простым, и код добавляет его в список простых чисел.
# Цикл while продолжается до тех пор, пока длина списка простых чисел не будет равна n. На этом этапе
# функция возвращает список простых чисел.
# ===========================================================================

# 8. Write a program that calculates the sum of the first 1000 Fibonacci numbers.
# RU: Напишите программу, которая вычисляет сумму первых 1000 чисел Фибоначчи.
def sum_fibonacci(n):
    сумма = 0
    предыдущее_число = 0
    текущее_число = 1
    for i in range(n):
        сумма += текущее_число
        предыдущее_число = текущее_число 
        текущее_число = предыдущее_число + текущее_число
    return сумма
    
# RU: Код выше - определяет функцию с именем sum_fibonacci, которая принимает целое число n в 
# качестве входных данных и возвращает сумму первых n чисел Фибоначчи. Функция использует цикл 
# for для генерации последовательности Фибоначчи, начиная с первых  двух чисел 0 и 1.
# Внутри цикла for код вычисляет сумму текущего числа Фибоначчи, которая является суммой двух 
# предыдущих чисел Фибоначчи. Затем код обновляет значения предыдущего и текущего чисел Фибоначчи 
# для подготовки к следующей итерации цикла.
# Цикл for продолжается до тех пор, пока он не сгенерирует n чисел Фибоначчи. На этом этапе функция 
# возвращает сумму чисел Фибоначчи.
# ==========================================================================================

# 9. Write a program that generates a random password of length 20.
# import random
# letters = "abcdefghijklmnopqrstuvwxyz"
# letters_upper = letters.upper()

# letters_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# letters_ru_upper = letters_ru.upper()

# numbers = "1234567890"
# symbols = "@#$%^&*"

# total_symbols_for_password = 20
# everything_included = letters + numbers + symbols + letters_ru

# created_password = ""
# for i in range(total_symbols_for_password):
#     random_int = random.randint(0, len(everything_included)-1)
#     created_password += everything_included[random_int]

# print(created_password)
# ===========================================================================



if __name__ == "__main__":
    pass