# DICTIONARIES  ==>>  Словари
# Словари - это структуры данных, которые хранят данные в виде пар ключ-значение.
# x = {
#     "first": ["Один", "..."],    "second": "Два",
#     2: True,     "fourth": "Четыре",
#     "fifth": 1,         "sixth": "Шесть",
#     7: False,  "eighth": {...},
# }
# # print(x)
# ==================================================================
# GETTERS  -> Методы получения значений
# print(x["first"]) # => ['Один', '...']
# print(x[1]) # => Error if not found
# # ----------------------------------
# print(x.get('first')) # => ['Один', '...']
# print(x.get(1)) # => None if not found
# print(x.get(1, "Не нашлось")) # => "Не нашлось" if not found
# print(x.get("fourth", "Не нашлось"))
# print(x["fourth"]) # => Четыре 
# print(x["www"]) # => # Error if not found
# ==================================================================
# - with lists
# z = [ "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь" ]
# for i in z:
#     if i == "Четыре":
#         print(i)
# -------------
# - with dictionaries
# print(x["fourth"]) # => Четыре

# NOTE:
# If there are 1000 doors, when using list and seeking some of them,
# the loop we are using, opens every door one by one to check them
# But, if we use dictionary here, it directly opens the needed one.
# RU: Если есть 1000 дверей, когда мы используем <list> и ищем 
# некоторые из них, цикл, который мы используем, открывает каждую дверь
# по одной, чтобы проверить их. Но, если мы используем здесь <dict>,
# он сразу же открывает нужную.
# ------------------------------------------------
# IN JAVA-SCRIPT
# function Person(name, ..., ...) {
#     this.name = name
#     this.name = name
#     this.name = name
#     ...
# }
# let person1 = new Person(..., ..., ...)
# ------------------------------------------------
# IN PYTHON
# dict()  =>  dict(key=value, key=value, key=value)
# person = dict(name='Kamron', bemiyya=True)
# print(person)
# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}


# # ACCESSING ITEMS ---------------------------------------------------------------------------
# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default

# Object.keys(dict) => возвращает список ключей (JS)
# dict.keys()       => возвращает список ключей

# Object.values(dict) => возвращает список ключей (JS)
# dict.values()     => возвращает список значений

# Object.entries(dict) => возвращает список ключей (JS)
# dict.items()      => возвращает список кортежей (ключ, значение)

# person1 = dict(name='Javox', bemiyya='True')
# print(list(person1.items()))


# # ADDING ITEMS -----------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# person1['bemiyya'] = True
# person1['...'] = "..."
# person1[1] = 1
# print(person1)
# -----------------
# Update => updates the dict (changes the original)
# dict.update({key:value, key:value, key:value})
# person1 = dict(name='Mirsaid', bemiyya=False)
# person1.update({
#     "name": "Alex", 
#     "bemiyya":True,
#     "address": "Samarkand", 
# })
# print(person1)
# -----------------
# ==========================================================================
# SETDEFAULT method

# If the key is not found, a new key:value pair is added to the dictionary.
# RU: Если ключ не найден, в словарь добавляется новая пара ключ: значение.

# But if it exists, then the value of the key is NOT updated.
# RU: Но если он существует, то значение ключа НЕ обновляется.
# dict.setdefault(key, value)
# person1 = dict(name='Mirsaid', bemiyya=False, address='...')
# person1.setdefault("address", "Tashkent")
# print(person1)


# # REMOVING ITEMS ---------------------------------------------------------------------------
person1 = dict(name='Mirsaid', bemiyya=False)

## dict.pop(key)
# del_val = person1.pop('name')
# print("del_val: ", del_val)
# print("person1: ", person1)
# -----------------------------------------
## dict.pop(key, default)
# res = person1.pop('www', None)
# print("Result: ", res)
# print(person1)
# -----------------------------------------
## dict.popitem() => removes the last inserted item
# res = person1.popitem()
# print("Result: ", res)
# print("Remaining: ", person1)
# -----------------------------------------
# del dict[key]
# del person1['bemiyya']
# del person1 # deletes the whole dict
# print("Remaining: ", person1)

# # MERGE ------------------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# person2 = dict(name="Covid", contageous=True)
# person3 = dict(name="Bemiyya", widespread=True)
# # {**dict1, **dict2, **dict3, **dict4}
# result = {**person1, **person2, **person3}
# print("New: ", result)

# a = {**person, **person2, **person3 } 
# works like spread operator in JS  ->  Работает как оператор spread в JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# dict.clear()
# for key, val in person.items():
#     person[key] = ""


# p = { "name": "John", "age": 20, "surname": "Khan", "address": "Samarkand" }

# p == p2  # True
# p is p2 == False

# dict.copy()
# person = p.copy()
# person.update({"name":"Ali"})
# print(p)
# print(person)

# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# zip() function
# zip(iterator1, iterator2, ...)
# Result: ...(zip object)  =>  (1, 'a'), (2, 'b'), (3, 'c')

# itr1 = list('abcdefghijklmnopqrstuvwxyz') # ['a', 'b', 'c', ...]
# itr2 = range(len(itr1))                   # [0, 1, 2, ...]
# zipped = zip(itr1, itr2)

# print(list(zipped))

# for (letter, index) in zipped:
#     print(letter, index)

# # --------------------------------------------------------------------------------------------
# # DICTIONARY COMPREHENSIONs-------------------------------------------------------------------

# # Using range() function and no input list
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)


# # Lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# # Using one input list
# numdict = {x:x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# # Using two input lists
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)
