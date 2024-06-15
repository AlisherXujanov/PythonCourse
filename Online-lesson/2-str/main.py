from turtle import st


string = "Hello, world!"
# -----------------------------------
# MIDDLE = len(string) // 2 
# print(string[MIDDLE+1])
# -----------------------------------
# DELETE THE MIDDLE CHARACTER
# RU: Удалить средний символ

# MIDDLE = len(string) // 2
# first = string[:MIDDLE]
# second = string[MIDDLE+1:]
# print(first + second)
# -----------------------------------
# GET 3 Characters from the middle
# RU: Получить 3 символа из середины
# string = "This is test string"
# MIDDLE = len(string) // 2
# print(string[MIDDLE-1] + string[MIDDLE] + string[MIDDLE+1])
# -----------------------------------
# GET 3 from the end of the string
# RU: Получить 3 символа с конца строки
# string = "This is test string"
# print(string[-3:])
# -----------------------------------
# string = "This is test string"
# first = string[3:6]
# second = string[-6:-3]
# print(first+second)
# -----------------------------------
string = "This is test string"
first = string[0]
last = string[-1]
middle = string[1:-1]

print(last+middle+first)
# -----------------------------------
# Slice   =>   Часть
# Syntax:   "..."[start:end:step]
#       default: [0 : length : 1]

# print(string[-2])
# print(string[2:5])
# print(string[:])
# print(string[:5])
# print(string[5:])
# print(string[2::2])
# print(string[::2])
# print(string[::-1])
# -----------------------------------
# second = string[1]
# former = string[-2]
# print("Second:", second, "Former:", former)
# -----------------------------------
