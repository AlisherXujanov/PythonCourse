# Decorators

# Let's create a Python decorator function named `performance`. This decorator is designed to measure the execution time of other functions. Here's how it should work:

# - **Input: ** The `performance` decorator accepts a single function as its argument.
# - **Wrapped Function**: The `performance` decorator should return a modified("wrapped") version of the input function that:
#     1. Records the * start * time before running the wrapped function
#     2. Executes the wrapped function and stores its resturn value
#     3. Records the * end * time after running the wrapped function
#     4. Calculates the elapsed time(end time - start time)
# - **Return Value: ** The wrapped function should return a ** tuple ** with:
#     1. The elapsed time ( in seconds) taken to execute the wrapped function
#     2. The wrapped function's return value
 
# The `time` module has a function named `perf_counter` for measuring how long it takes to run something. For example:

# ```python
# import time

# start_time = time.perf_counter()     # "Start" timer
# time.sleep(1)                        # Wait one second
# end_time = time.perf_counter()       # "Stop" timer
# elapsed_time = end_time - start_time # should be *slightly* more than 1

# print(elapsed_time) # 1.0045422080000037 (approximately)
# ```

# Define a decorator named `performance` that wraps a function to return a **tuple** with (1) the original return value of the function and (2) the amount of time that it took. For example, we should be able to write:

# ```python
# @performance
# def add(a, b):
#     return a + b

# sum_result, time_taken = add(1, 2) # sum_result == 3, time_taken ~= 0
# ```


# *Hint: to create a decorator named `fake_performance` that returns a tuple with the function call result and a string, we could do the following:*

# ```python
# import functools

# def fake_performance(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result, "PUT THE ELAPSED TIME HERE AS A NUMBER"
#     return wrapper
# ```


# YOUR CODE HERE
import time
import functools

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper

@performance
def add(a, b):
    return a + b

sum_result, time_taken = add(1, 2)
print(sum_result, time_taken)

# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================


