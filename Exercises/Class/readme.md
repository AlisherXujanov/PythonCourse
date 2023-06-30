# Dunders

- Dunders are the methods that start with double 
  underscore '__' and end with double underscore '__' 
  and they are also called magic methods.
  RU: Дандеры - это методы, которые начинаются с двойного 
  подчеркивания '__' и заканчиваются двойным подчеркиванием '__' и их также называют магическими методами.
- Dunders are used to emulate some built-in behaviour within python.
  (ex: operator overloading or __init__ method or __repr__, __str__ methods ...)
  RU: Дандеры используются для эмуляции некоторого встроенного поведения внутри python
  (например: перегрузка операторов или методы __init__, __repr__, __str__ ...)

#### METHODS
1. __init__ method - is used to initialize the object.
   RU: метод __init__ - используется для инициализации объекта.
2. __call__ method - is used to call the object like a function.
   RU: метод __call__ - используется для вызова объекта как функции.
3. __repr__ method - is used to return the string representation of the object.
4. __str__ method - is used to return the string representation of the object.
5. __add__ method - is used to add two objects.
...

#### EXAMPLES
```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Employee('{self.name}', {self.age})"

    def __str__(self):
        return f"Employee name: {self.name}, age: {self.age}"

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return len(self.name)
```

---

