# BUILT IN FUNCTIONS
# =======================================================================================

# 1. Create a function that sums up all the numbers in a list and compare 
# it with the highest number from the same list. Then, get the difference and 
# show the message that if it is even or odd number.
# RU: Создайте функцию, которая суммирует все числа в списке и сравнивает
# это с самым большим числом из того же списка. Затем получите разницу и
# покажите сообщение, четное это число или нечетное.
def sum_and_compare(arr):
    total = sum(arr)
    max_num = max(arr)
    difference = total - max_num
    even_or_odd = 'even' if difference % 2 == 0 else 'odd'
    return f"Total: {total}, Max: {max_num}, Difference: {difference} and it is {even_or_odd}"
# print(sum_and_compare([1, 2, 3, 4, 5]))

# =======================================================================================

# 2. Create a function that takes a list of numbers and returns third biggest.
# RU: Создайте функцию, которая принимает список чисел и возвращает третий по величине.
def third_smallest(list):
    list_copy = list.copy()
    highest = max(list)
    list_copy.remove(highest)
    second_highest = max(list_copy)
    list_copy.remove(second_highest)
    return max(list_copy)
    # second_highest = max([x for x in list if x != highest])
    # return max([x for x in list if x != highest and x != second_highest])

# =======================================================================================

# 3. Create a function that gets only numbers from given sentence and 
# separates them into two lists: evens and odds 
# RU: Создайте функцию, которая получает только числа из данного предложения и
# разделяет их на два списка: четные и нечетные
# Use at least one built-in function 
# RU: Используйте по крайней мере одну встроенную функцию

# INPUT: "Hello 7th World in 2023 year 2nd time"
# [7, 3] [2, 0, 2]
def even_odd(sentence):
    numbers = [int(x) for x in sentence.split() if x.isdigit()]
    odds = []
    evens = []
    for num in numbers:
        if num%2==0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds

# =======================================================================================

# 4. Create a function that accepts a string and counts the number of 
# upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# ---------------------------------
# RU: Создайте функцию, которая принимает строку и подсчитывает количество
# прописных и строчных букв.
# Пример строки: 'The quick Brow Fox'
# Ожидаемый результат:
# Количество прописных букв: 3
# Количество строчных букв: 12
def upper_lower(sentence):
    upper = 0
    lower = 0
    for letter in sentence:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return f"Upper: {upper}, Lower: {lower}"


# =======================================================================================

# 5. Create a function that counts vowel and consonant letters in a string.
# RU: Создайте функцию, которая подсчитывает гласные и согласные буквы в строке.
def vowels_and_constants(sentence):
    vowels = 0
    constants = 0
    for letter in sentence:
        if letter in 'aeiou':
            vowels += 1
        elif letter.isalpha():
            constants += 1
    return f"Vowels: {vowels}, Constants: {constants}"

# =======================================================================================
# 6. Write a program that takes a list of numbers as input and 
# returns the sum of the even numbers.
# RU: Напишите программу, которая принимает список чисел в качестве входных 
# данных и возвращает сумму четных чисел.
def sum_even_nums():
    numbers_as_str = input("Enter numbers separated by comma ',': ").split(',')
    total = []
    for num in numbers_as_str:
        num = num.strip()
        if num.isnumeric():
            if int(num)%2==0:
                total.append(int(num))
    # total_list_of_numbers = [x.strip() for x in numbers_as_str if x.strip().isnumeric()]
    # total = filter(lambda x: total.append(x) if x%2==0 else 0, total_list_of_numbers)
    return sum(total)
# =======================================================================================
# 7. Write a program that takes a list of strings as input and returns the longest string.
# RU: Напишите программу, которая принимает список строк в качестве входных
# данных и возвращает самую длинную строку.
def longest_word():
    print(max(input("Enter words separated by comma ',': ").split(','), key=len))

# =======================================================================================
# 8. Write a program that takes a string as input and returns the number of letters in each string.
# RU: Напишите программу, которая принимает строк в качестве входных данных 
# и возвращает количество букв в каждой строке.
def letters_in_string():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(map(lambda x: len(x.strip()), words)))

# =======================================================================================
# 9. Write a program that takes a list of numbers as input and 
# returns the average of the numbers.
# RU: Напишите программу, которая принимает список чисел в качестве 
# входных данных и возвращает среднее значение чисел.
def average_of_numbers():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    print(round(sum([int(x.strip()) for x in numbers]) /  len(numbers)))

# =======================================================================================
# 10. Write a program that takes a string as input and returns the string with all vowels removed.
# RU: Напишите программу, которая принимает строку в качестве входных 
# данных и возвращает строку без гласных.
def words_without_vowels():
    vowels = 'aeiou'
    words = input("Enter words separated by comma ',': ").split(',')
    
    def remove_vowel(word):
        return "".join([letter for letter in word if letter.lower() not in vowels])
    print(list(map(remove_vowel, words)))

    # words = [x for x in words if x not in vowels]
    # return ''.join(words)

# =======================================================================================
# 11. Write a program that takes a list of strings as input and returns a new list with all strings capitalized.
# RU: Напишите программу, которая принимает список строк в качестве входных данных и возвращает
# новый список со всеми строками прописными.
def capitalized_words():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(map(lambda x: x.capitalize(), words)))

# =======================================================================================
# 12. Write a program that takes a list of numbers as input and returns the largest number.
# RU: Напишите программу, которая принимает список чисел в качестве входных данных и возвращает
# самое большое число.
from functools import reduce
def largest_number():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    print(max(numbers))
    # Using reduce()
    print(reduce(lambda x, y: x if x > y else y, numbers))

# =======================================================================================
# 13. Write a program that takes a list of strings as input and returns a new list with 
# all strings of length 4 or greater.
# RU: Напишите программу, которая принимает список строк в качестве входных данных и возвращает
# новый список со всеми строками длиной 4 или больше.
def words_length():
    words = input("Enter words separated by comma ',': ").split(',')
    print(list(filter(lambda x: len(x.strip()) >= 4, words)))

# =======================================================================================

# 14. Write a function that takes a list of integers as input 
# and returns the sum of the squares of the even numbers 
# in the list. Use the reduce() function to perform the calculation.
# RU: Напишите функцию, которая принимает список целых чисел 
# в качестве входных данных и возвращает сумму квадратов четных
# чисел в списке. Используйте функцию reduce() для выполнения вычислений.

# INPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >> 2**2 + 4**2 + 6**2 + 8**2 = 120
# OUTPUT: 120
def sum_of_squares():
    numbers = input("Enter numbers separated by comma ',': ").split(',')
    print(reduce(lambda x, y: x + y, map(lambda x: int(x.strip())**2 if int(x)%2==0 else 0, numbers)))
    print("This is function")

# =======================================================================================
# =======================================================================================

# Use map() to convert a list of strings to a list of integers.
# RU: Используйте map(), чтобы преобразовать список строк в список целых чисел.

# INPUT:   ["www", "12345", "qwe", 124, '54321', 'aaaaa']
# OUTPUT:  [3, 12345, 3, 124, 54321, 5]

def get_as_nums(arr:list) -> list:

    def get_as_num(val) -> int:
        if type(val) == int:
            return val
        elif val.isnumeric():
            return int(val)
        else:
            return len(str(val))
            
    return map(get_as_num, arr)
    
test_arr = ["www", "12345", "qwe", 124, '54321', 'aaaaa']
total = get_as_nums(test_arr)
print(list(total))


# =======================================================================================
# Use filter() to remove all odd numbers from a list.
# RU: Используйте filter(), чтобы удалить все нечетные числа из списка.



# =======================================================================================
# Use map() and filter() together to convert a list of 
# strings to a list of integers and then remove all odd numbers.
# RU: Используйте map() и filter() вместе, чтобы преобразовать 
# список строк в список целых чисел, а затем удалить 
# все нечетные числа.
def map_and_filter(arr:list) -> list:

    def get_as_num(val) -> int:
        if type(val) == int:
            return val
        elif val.isnumeric():
            return int(val)
        else:
            return len(str(val))
            
    return filter(lambda x: x%2==0,  map(get_as_num, arr))
    
    
test_arr = [22, "wwww", "12345", "qwe", 124, '54321', 'aaaaa']
# print(list(map_and_filter(test_arr)))




if __name__ == "__main__":
    """
    This is the main function that calls other functions.
    """
    # print(vowels_and_constants("Hello World!"))
    # print(sum_even_nums())
    # longest_word()
    # letters_in_string()
    # average_of_numbers()
    # words_without_vowels()
    # capitalized_words()
    # largest_number()
    # words_length()
    # sum_of_squares()
