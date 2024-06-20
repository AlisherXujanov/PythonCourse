# 1. Напишите функцию, чтобы перевернуть строку.
# [start:stop:step]

# x = "Damirjon"
# print(x[0:4])
# print(x[::-1])
# print("Amirbek"[::-1])

# -------------------------------------
# 2. Напишите функцию, чтобы удалить символ с индексом n из непустой строки.
# integer = 1
# string = "Amirbek"  # => "Helo, world!"
# first = string[0:integer]
# last = string[integer+1:]
# print(first+last)
# -------------------------------------
# 3. Напишите функцию, чтобы удалить символы, 
# которые имеют нечетные индексы заданной строки.
# text = "Hello world"
# print(text[1::2])
# -------------------------------------
# 4. Напишите функцию, чтобы проверить, 
# является ли заданная строка палиндромом.
# 'madam' => True
# 'hello' => False
# text = "Hello world"
# text2 = "madam"

# print("Hello world: ",  text  == text[::-1])
# print("Madam: ",        text2 == text2[::-1])
# -------------------------------------
# text = "Hello world of universe" # ["Hello", "world", "of", "universe"]

# first = text[0]
# last = text[-1]
# middle = text[1:-1]

# print(last+middle+first)

# first_word = text.split()[0]
# last_word = text.split()[-1]
# middle_word = text.split()[1:-1]  # ->   ["world", "of"]   ->  "world of"

# print(last_word, " ".join(middle_word), first_word)
