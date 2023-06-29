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


# ==========================================================================================
# ==========================================================================================
# 2. Print stars (*) in the shape of a pyramid with N number of steps.
# pyramid(4) =>
#    *
#   ***
#  *****
# *******
def pyramid(n):
    for i in range(n):
        print(' '*(n-i-1)   +   '*'*(i * 2 + 1))


# ==========================================================================================
# ==========================================================================================
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

# ==========================================================================================
# ==========================================================================================
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
# ==========================================================================================
# ==========================================================================================
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

    
# ==========================================================================================
# ==========================================================================================
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

# ==========================================================================================
# ==========================================================================================

# 7. Write a program that prints out the first 100 prime numbers.
# RU: Напишите программу, которая выводит первые 100 простых чисел.
prime_numbers = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
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

# RU: Код выше - определяет функцию с именем n_prime_numbers, которая
# принимает целое число n в качестве входных данных и возвращает список первых n простых чисел.
# Функция использует цикл while для генерации простых чисел, начиная с первого простого числа 2.
# Внутри цикла while код проверяет, является ли текущее число простым, перебирая все целые числа
# от 2 до текущего числа - 1. Если текущее число делится на любое из этих чисел, то оно не является
# простым, и код устанавливает логический флаг is_prime в False. Если текущее число не делится на
# любое из этих чисел, то оно является простым, и код добавляет его в список простых чисел.
# Цикл while продолжается до тех пор, пока длина списка простых чисел не будет равна n. На этом этапе
# функция возвращает список простых чисел.
# ==========================================================================================
# ==========================================================================================

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
# ==========================================================================================

# 9. Write a program that generates a random password of length 20.
import random


def create_password_of_length(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_upper = letters.upper()     # NOTE:  Can be included for making the password more secure

    letters_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    letters_ru_upper = letters_ru.upper()  # NOTE:  Can be included for making the password more secure

    numbers = "1234567890"
    symbols = "@#$%^&*"

    everything_included = letters + numbers + symbols + letters_ru

    created_password = ""
    for i in range(length):
        random_int = random.randint(0, len(everything_included)-1)
        created_password += everything_included[random_int]
    print(created_password)
    return created_password

# ==========================================================================================
# ==========================================================================================

# 10. Guessing Game Two
#     In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#     This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
#     The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#     At the end of this exchange, your program should print out how many guesses it took to get your number.
#     As the writer of this program, you will have to choose how your program will strategically guess.
#     A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
#     But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range),
#     and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
def guessing_game_two():
    print("Think of a number between 0 and 100")
    low = 0
    high = 100
    guess = 50
    tries = 0
    while True:
        print(f"Is your number {guess}?")
        answer = input(
            "Enter 'h' if the guess is too high, 'l' if too low, or 'c' if correct: ")

        tries += 1
        if answer == 'h':
            high = guess
            guess = (low + high) // 2
        elif answer == 'l':
            low = guess
            guess = (low + high) // 2
        elif answer == 'c':
            print("I guessed your number in {} tries!".format(tries))
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

# ==========================================================================================
# ==========================================================================================

# 11. Draw A Game Board
#     Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#     --- --- ---
#     |   |   |   |
#     --- --- ---
#     |   |   |   |
#     --- --- ---
#     |   |   |   |
#     --- --- ---
#     This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#     Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
def draw_board(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * (size+1))
    print(" ---" * size)
# ==========================================================================================
# ==========================================================================================

# MAGIC LAND GAME  => ПОЛЕ ЧУДЕС
import random


def pick_word():
    with open("sowpods.txt", "r") as f:
        words = f.readlines()
    return random.choice(words).strip()


def guess_letters():
    word = pick_word()
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("Guess letter: ")
    tries = 0
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
            print("Well guessed!!")
        else:
            tries += 1
            print(f"Wrong!! You have {6 - tries} tries left")

        print(''.join(guessed))
        if letter != '':
            lstGuessed.append(letter.upper())

        letter = input("Guess letter: ")

        if '_' not in guessed:
            print("You won!!")
            break
        elif tries == 6:
            print("You lost!!")
            break

guess_letters()
# ==========================================================================================
# ==========================================================================================
