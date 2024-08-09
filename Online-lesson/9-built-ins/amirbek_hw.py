
# 1 Напишите функцию Python, которая отфильтровывает четные числа из
# списка целых чисел, используя функцию фильтра.
def filter_odd_nums(nums):
    def is_odd(num):
        return num % 2 != 0
    odd_nums = list(filter(is_odd, nums))
    return odd_nums


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original numbers:", nums)
result = filter_odd_nums(nums)
print("After filters out even numbers from the said list of integers ")
print(result)  # Output: [1, 3, 5, 7, 9]
# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# 2 Напишите программу на Python, которая использует функцию фильтра для извлечения всех заглавных букв из списка строк в смешанном регистре.


def filter_numbers_less_than(numbers, threshold):
    def is_less_than_threshold(num):
        return num <= threshold
    filtered_numbers = list(filter(is_less_than_threshold, numbers))
    return filtered_numbers


numbers = [20, 15, 24, 37, 23, 11, 7]
print("Original list of numbers:", numbers)
threshold = 20
print("\nFilters out all elements less than or equal to a specified value", threshold, ":")
result = filter_numbers_less_than(numbers, threshold)
print(result)


# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# 3. изменить_первый_символ
def change_first_char(symbol: str = "$", text='') -> str:
    if len(text) > 0:
        string = text
    else:
        string = input("Напишите любое слово: ")

    first = string[0]
    return first + string[1:].replace(first.lower(), symbol)

r = change_first_char(text="This is test text")  # "This is $es$ $ex$"
print(r)


# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# 4. является_палиндромом
def is_palindrome(string):
    return string == string[::-1]

# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# ===========  ===========  ===========  ===========  ===========  ===========  ===========
# 5. you have text and you should change last vowel into - (dash)
# RU: у вас есть текст и вы должны изменить последнюю гласную на - (тире)

def change_last_vowel_to_dash(text):
    vowels = 'aouie'
    last_vowel = ''
    # We must find the last vowel in the text
    # RU: Мы должны найти последнюю гласную в тексте
    for i in text[::-1]:
        if i in vowels: 
            last_vowel = i
            break

    idx_of_last_vowel = text.rfind(last_vowel)
    return text[0:idx_of_last_vowel] + '-' + text[idx_of_last_vowel + 1:]

r = change_last_vowel_to_dash("Hello world") # Hello w-rld      
print(r)


