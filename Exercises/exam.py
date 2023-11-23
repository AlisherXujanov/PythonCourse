# EXAM EXERCISES
# 1. Create a function that finds n number of prime numbers.
# RU: Создайте функцию, которая находит n количество простых чисел.
# 2. Create a function that counts how much time that 
# function takes to execute.
# RU: Создайте функцию, которая подсчитывает, сколько 
# времени занимает выполнение этой функции.
# 3. Create a class that takes this function as a method 
# and returns the execution time. Then, create an object
# and call the method.
# RU: Создайте класс, который принимает эту функцию в 
# качестве метода и возвращает время выполнения. Затем
# создайте объект и вызовите метод.


def prime_numbers(n):
    result = []
    current_num = 1
        # METHOD 1
    while len(result) < n:
        current_num += 1
        # METHOD 1
        # for i in range(2, current_num):
        #     if current_num % i == 0:
        #         break
        # else:
        #     result.append(current_num)
        # -------------------------------
        # METHOD 2
        # if current_num % 2 != 0 and current_num % 3 != 0 and current_num % 5 != 0 and current_num % 7 != 0:
        #     result.append(current_num)
        # -------------------------------
        # METHOD 3
        if all(current_num % i != 0 for i in range(2, current_num)):
            result.append(current_num)

    return result
