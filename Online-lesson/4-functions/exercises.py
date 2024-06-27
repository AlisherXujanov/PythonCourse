# ------------------------ BEGINNER ------------------------
# 14. Напишите программу, которая принимает список чисел
# (например, a=[5, 10, 15, 20, 25]) и создает новый список 
# только первого и последнего элементов заданного списка.
# ------------------------------
# def first_last(arr):
#     return [arr[0], arr[-1]]


# first_last([5, 10, 15, 20, 25]) # [5, 25]
# first_last([100, 10, 15, 20])   # [100, 20]
# ==========================================================
# ==========================================================



# ------------------------ INTERMEDIATE ------------------------
# 2. Напишите функцию, которая принимает сортированный список чисел
# (список, в котором элементы сортированы от наименьшего к наибольшему)
# и другое число. Функция решает, находится ли заданное число в списке, 
# и возвращает(затем печатает) соответствующий булевый результат. 
# (Используйте бинарный поиск.)

from operator import indexOf


def check_if_includes(arr:list, number:int) -> bool:
    return number in arr
    # --------------------
    # BINARY SEARCH
    # ...
    

check_if_includes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)    # True
check_if_includes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100)  # Fasle



# ------------------------ ADVANCED ------------------------
# 7. Напишите функцию, которая принимает строку и возвращает новую строку, 
# в которой каждая гласная заменена на следующую гласную в алфавите.

vowels = "aeiou"
text = "Hello u"

def change_vowel_into_next(string:str) -> str:
    result = ""
    for letter in string:
        if letter in vowels:
            indexOfLetter = vowels.index(letter)
            if indexOfLetter == len(vowels) - 1:
                neededLetter = vowels[0]
            else:
                neededLetter = vowels[indexOfLetter + 1]
            result += neededLetter
        else:
            result += letter
    return result

result = change_vowel_into_next(text) # "Hillu"
print(result)


