# def get_max(a, b) -> int:
#     return a if a > b and a > c else (b if b > c and b > a else c)

    
# a = 1
# b = 2
# c = 3 
# r = get_max(a, b, c)
# print(r)

# l = [1,2,3,4,5,6,7,8,9,10]
# r = list(range(1,10,2))

# text = "Hello, this is 3rd task 9 1 2 "
# result = [num for num in text if num.isnumeric()] 



print("================================================")
names = ["Вася", "Петя", "Коля", "Ваня", "Amir"]
# {"Name": "Ва", "Surname": "ся"}
# {"Name": "Пе", "Surname": "тя"}


# {"Name": "Вася", "Surname": "Вася-ov"}
dicts = []
for name in names:  # Каждый элемент в списке принимает называние name
   d = dict(name=name, surname= f"{name}sya")  # Создаем словарь с ключами name и surname..
print(dicts)  # Выводим список dicts