# Question: 1
# Write a function called int_return that takes an integer as input and returns the same integer.
# Solution:
def int_return(num):
    return num


print(int_return(10))
# =================================================================================
# =================================================================================
# Question: 2
# Write a function called add that takes any number as its input and returns that sum with 2 added.
# Solution:


def add(num):
    return num+2


print(add(6))
# =================================================================================
# =================================================================================
# Question: 3
# Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new
# string.
# Solution:


def change(string):
    return string+"Nice to meet you!"


print(change("I'm Bob. "))
# =================================================================================
# =================================================================================
# Question:4
# Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
# Solution:


def accum(lst):
    s = 0
    for ele in lst:
        s += ele
    return s


print(accum([2, 4, 6, 8]))
# =================================================================================
# =================================================================================
# Question:5
# Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer
# than 5”. If the length is less than 5, return “Less than 5”.
# Solution:


def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"


print(length([1, 1, 1, 1, 1]))
# =================================================================================
# =================================================================================
# Question:6
# You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number
# divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number.
# You should call the divide function within the sum function. Do not worry about decimals.
# Solution:


def divide(num1):
    return num1/2


def add(num2):
    return divide(num2)+6
