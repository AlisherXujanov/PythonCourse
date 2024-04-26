# 1. Basic Encapsulation Create a class Person with private attributes name and age. 
# Use getter and setter methods to access and modify these attributes.
# RU: Создайте класс Person с закрытыми атрибутами name и age.
# Используйте методы getter и setter для доступа и изменения этих атрибутов.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# =================================================================================================================
# 2. Encapsulation with Property Decorators Modify the Person class from Exercise 1 to use 
# @ property and @ < attribute > .setter decorators for encapsulation.
# RU: Измените класс Person из упражнения 1, чтобы использовать декораторы @ property и @ <attribute>.setter для инкапсуляции.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

# =================================================================================================================
# 3. Encapsulation with Validation Create a class BankAccount with a private attribute balance. 
# Implement a method to deposit money into the account. Use encapsulation to ensure that the 
# balance cannot be set to a negative value.
# RU: Создайте класс BankAccount с закрытым атрибутом баланс.
# Реализуйте метод для внесения денег на счет. Используйте инкапсуляцию, чтобы гарантировать,
# что баланс не может быть установлен в отрицательное значение.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

# =================================================================================================================
# 4. Encapsulation with Inheritance Create a class Employee that inherits from the Person class 
# in Exercise 1. Add a new private attribute salary to the Employee class . Use encapsulation to access and modify salary.
# RU: Создайте класс Employee, который наследует от класса Person из упражнения 1.
# Добавьте новый закрытый атрибут salary в класс Employee. Используйте инкапсуляцию для доступа и изменения зарплаты.
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary


# =================================================================================================================
# 5. Encapsulation with Complex Objects Create a class Car with private attributes make, model, 
# and year. Create a class Garage with a private attribute cars that stores a list of Car objects. 
# Use encapsulation to add, remove, and list cars in the garage.
# RU: Создайте класс Car с закрытыми атрибутами make, model и year.
# Создайте класс Garage с закрытым атрибутом cars, который хранит список объектов Car.
# Используйте инкапсуляцию для добавления, удаления и перечисления автомобилей в гараже.
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def __str__(self):
        return f"{self.__year} {self.__make} {self.__model}"
    

class Garage:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        if isinstance(car, Car):
            self.__cars.append(car)
        else:
            raise TypeError("Object is not of type Car")

    def remove_car(self, car):
        if car in self.__cars:
            self.__cars.remove(car)
        else:
            raise ValueError("Car not found in garage")

    def list_cars(self):
        return self.__cars