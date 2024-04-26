# Напишите функцию для извлечения уникальных символов или букв (которые только 1 раз указаны) из строки 

text = "This is test text"

def unique_symbols(text:str) -> str:
    result = ""
    for letter in text:
        if letter not in result:
            result += letter.lower()
    return result


print(unique_symbols(text))