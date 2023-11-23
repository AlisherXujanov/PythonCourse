import math
import time

def fn_1():
    print("Function first")


def fn_2():
    print("Function Second")


def fn_3(fn):
    print('-----------------------------------')
    print("Befor calling {}".format(fn.__name__))
    fn()
    print("After calling {}".format(fn.__name__))


fn_3(fn_1)
fn_3(fn_2)
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

lesson = "Decorators & Wrappers"
# Decorators are functions that take another function as an argument, add some kind of functionality,
# and then return another function. All of this without altering the source code of the original
# function that we passed in. In Python, functions are first-class objects, which means that we can
# pass them as arguments to other functions. We can also return them as the values from other functions.
# This is the basis of decorators.

# SYNTAX
# def decorator_function(original_function):
#     def wrapper_function(): # RU: обертка => та функция которая покрывает оригинальную функцию
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print("Display function ran")

# display() == decorator_function(display)()

####################################################################################
####################################################################################
####################################################################################
# BASIC DECORATOR


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def original_function():
    print("Original function ran")

####################################################################################
# defining a decorator


def декоротивная_функция(func):

    def покрывала_функции():
        print("Это до выполнения функции")
        result = func() # RU: вызов оригинальной функции
        print("Это после выполнения функции")
        return result
    return покрывала_функции


# Создание оригинальной функции
def оригинальная_функция():
    print("Это призвано быть оригинальной функцией")


функция_для_использования = декоротивная_функция(оригинальная_функция)

# Призив оригинальной функции
функция_для_использования()


####################################################################################
####################################################################################
####################################################################################
# Practical example 1
# find out the execution time of a function using a decorator.

# decorator to calculate duration
# taken by any function.
def calculate_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)

####################################################################################
####################################################################################
####################################################################################
# RETURN A VALUE

def hello_decorator(func):
    def inner1(*args, **kwargs):

        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
sum = sum_two_numbers(a, b)
print("Sum =", sum)
####################################################################################
####################################################################################
####################################################################################
# MEMOIZATION
# Factorial program with memoization using decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}


def memoize_factorial(f):

    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)


print(facto(5))
print(facto(5))  # directly coming from saved memory
print(memory)

####################################################################################
####################################################################################
####################################################################################
# MEMORY USAGE CHECK

def measure_memory(fn):
    def wrapper(*args, **kwargs):
        import memory_profiler

        # install memory_profiler with pip install memory_profiler
        result = memory_profiler.memory_usage()
        in_kilobytes = result[0]
        print(f"Memory used before running {fn.__name__}: {in_kilobytes} kb")

        # memory usage shows the memory usage of the current process in kilobytes
        return result
    return wrapper


@measure_memory
def test_fn6(string):
    print("Inside the original function")
    return string
