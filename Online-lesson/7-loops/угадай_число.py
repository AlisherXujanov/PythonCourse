import random

RANDOM_NUMBER = random.randint(1, 100)   # 1-100
LIVES = 7  # количество попыток


def show_text(message):
    print("======================================")
    print(message)
    print("======================================")


show_text("""
--------------------------------------
✋Добро пожаловать в игру "Угадай число" 🔢!
Вам нужно угадать число от 1 до 100.  💥        
--------------------------------------
""")

guessed_numbers = [] # список угаданных чисел


while LIVES > 0:
    answer = input('Угадайте число от 1 до 100: 👉  ')
    if answer.isnumeric():
        num = int(answer)
        if 1 <= num <= 100:

            if num in guessed_numbers:
                show_text("Вы уже вводили это число! Введите другое число...")
                continue
            else:
                # добавить число в список угаданных
                guessed_numbers.append(num)
    
    
            if num == RANDOM_NUMBER:
                show_text("Поздравляю! Вы победили!")
                break
            else:
                LIVES -= 1
                if num > RANDOM_NUMBER:
                    show_text("Слишком много! Осталось попыток: " +
                              str(LIVES) + ". Попробуйте еще раз...")
                else:
                    show_text("Слишком мало! Осталось попыток: " +
                              str(LIVES) + ". Попробуйте еще раз...")
        else:
            show_text("Введите число между 1 и 100 !!!")
    else:
        show_text("Введите только ЧИСЛО между 1 и 100 !!!")


if LIVES == 0:
    show_text("""
Игра окончена! 😮
Загаданное число было: 😔  """ +
              str(RANDOM_NUMBER))
