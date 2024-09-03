# FUNCTIONS 

# -------------------------- INTERMEDIATE --------------------------
# 1. ... 
# ------------------------
# ------------------------
# 2. Напишите функцию, которая принимает строку в качестве параметра и преобразует первую букву каждого слова строки в верхний регистр.      

def create_title(text:str) -> str:
    splitted_text = text.split(" ") # ["hello,", "my", "name", "is", ...]
    pool = ''
    for word in splitted_text:
        pool += word.capitalize() + " "
    return pool

text = "hello, my name is amirbek and i am a programmer"
r = create_title(text)
# print(r)
    
# ------------------------
# ------------------------
# 3. ...
# ------------------------
# ------------------------
# 4. Напишите функцию, которая принимает строку в качестве параметра и подсчитывает количество гласных в строке. 
def count_vowels(text:str) -> int:
    vowels = 'aeiou'
    pool = 0
    
    for letter in text:
        if letter in vowels:
            pool += 1   
    
    return pool

r = count_vowels("hello, my name is amirbek and i am a programmer")
# print(r)

# ------------------------
# ------------------------
# 5. ...
# ------------------------
# ------------------------

# -------------------------- ADVANCED --------------------------
# 1. Напишите функцию для извлечения уникальных символов или букв (которые только 1 раз указаны) из строки 
def get_uniques(text:str) -> str:
    pool = ''
    for letter in text:
        if text.count(letter) == 1:
            pool += letter
    return pool

r = get_uniques("hello, my name is amirbek and i am a programmer")
# print(r)
# ------------------------
# ------------------------
# 2. ...
# ------------------------
# ------------------------
# 3. Напишите функцию, которая принимает массив строк. Функция должна вернуть новый массив, в котором каждая строка перевернута. 

def reverse_each_word(arr:list[str]) -> list[str]:
    pool = []
    for word in arr:
        reversed_word = word[::-1]
        pool.append(reversed_word)
    return pool

arr = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# output: ['elppa', 'ananab', 'yrrehc', 'etad', 'yrrebredle']

r = reverse_each_word(arr)
# print(r)
# ------------------------
# ------------------------
# 4. ...
# ------------------------
# ------------------------
# 5. Напишите функцию, которая принимает строку и возвращает символ, который появляется больше всего раз. 
def get_most_frequent(text:str) -> str:
    memory = text[0]
    for letter in text:
        if text.lower().count(memory) < text.lower().count(letter.lower()):
            memory = letter.lower()
    return memory

# banana = a
# cherry = r
# school = o
# This is test text = t
r = get_most_frequent("This is test text")
print(r)
# ------------------------


