# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for letter in l:
#     print(letter.upper())
# ---------------------------------------------------------------------
# words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry',
#               'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

# result = ""
# for word in words_list:
#     if len(word) > len(result):
#         result = word
# print(result)
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# result = []
# num = int(input("Enter a number: "))
# result.append(num)   # Само число
# result.append(num/2) # Половина числа
# result.append(num/4) # Четверть числа

# print(sum(result))
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# слова = ['apple', 'banana', 'cherry', 'date', 'elderberry',]
# с = input("Enter a word: ")

# MIDDLE = len(слова) // 2  #  2.5 =>  2
# слова.insert(MIDDLE, с)
# print(слова)  # ['apple', 'banana', 'word', 'cherry', 'date', 'elderberry']

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Создайте массив чисел. Найдите максимальное число(например, 12345), 
# затем сложите каждую цифру в числе(например, 1 + 2 + 3 + 4 + 5=15).

arr = [1241, 324, 123, 1234, 12345]
max_num = max(arr)

pool = []

for i in str(max_num):
    pool.append(int(i))

print(sum(pool))

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
