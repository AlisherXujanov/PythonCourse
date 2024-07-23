# DICTIONARY  => Словарь
# x = {
#     "key":"value",    
#     "key2":"value2",    
#     "key3":"value3",
# }
# print("-----------------------------")
# print(x["key4"]) # KeyError: 'key4'
# print(x.get("key4", "Не найдено"))
# print("-----------------------------")
# user = {
#     id: 1,
#     "username": "admin",
#     "email": "test@gmail.com",
#     "password": "123456",
#     "email": "Updated@gmail.com"
# }
# email = user.get("email", "Вася")
# print("-----------------------------")
# print(email)
# print("-----------------------------")
user = {
    id: 1,
    "username": "Вася",
    "email": "test@gmail.com",
    "password": "123456",
}
# print("================================")
# Добавление нового ключа
# user["surname"] = "Petrov"
# print(user)
# print("================================")
# Изменение значения ключа
# user["surname"] = "Ivanov"
# print(user)
# print("================================")
# del user["email"]
# print(user)
# print("================================")
# users = [
#     {"name": "Вася", "email": "@gmail.com", "password": "123456"},
#     {"name": "Петя", "email": "@gmail.com", "password": "123456"},
#     {"name": "Коля", "email": "@gmail.com", "password": "123456"},
#     {"name": "Ваня", "email": "@gmail.com", "password": "123456"},
#     {"name": "Amir", "email": "@gmail.com", "password": "123456"},
# ]
# for user in users:
#     print("-----------------------")
#     print(f"Name: {user['name']}.  Email: {user['email']}.  Password: {user['password']}")

# Fullname
# Вася .... Email: ..... Password: ....
# Петя .... Email: ..... Password: ....
# Коля .... Email: ..... Password: ....
# Ваня .... Email: ..... Password: ....
# Amir .... Email: ..... Password: ....


print("================================================")
names = ["Вася", "Петя", "Коля", "Ваня", "Amir"]
# {"Name": "Ва", "Surname": "ся"}
# {"Name": "Пе", "Surname": "тя"}


# {"Name": "Вася", "Surname": "Вася-ov"}
dicts = []
for name in names:  # Каждый элемент в списке принимает называние name
    # d = dict(name=name, surname=f"{name}ov")  # Создаем словарь с ключами name и surname
    # dicts.append(d)  # Добавляем словарь d в список dicts
    # -------------------------------------------------------------------
    d = dict(name=name[:2], surname=name[2:])  # Создаем словарь с ключами name и surname
    dicts.append(d)  # Добавляем словарь d в список dicts

print(dicts)  # Выводим список dicts