# 1. Write a Python program to calculate the sum of a
# list of numbers using recursion.
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

# ex:
# print(sum_list([1, 2, 3, 4, 5]))  # 15

# ---------------------------------------------------------
# 2. Write a Python program to convert an integer to a string
# in any base using recursion .


def int_to_string(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    else:
        return int_to_string(num // base, base) + convert_string[num % base]


# ex:
# print(int_to_string(2835, 16))  # B13
# ---------------------------------------------------------
# 3. Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3, 4], [5, 6]]
# Expected Result: 21
def sum_recursion_list(lst):
    # ============================================================
    # ------------------------- METHOD 1 -------------------------
    # return sum(sum_recursion_list(x) if isinstance(x, list) else x for x in lst)

    # ============================================================
    # ------------------------- METHOD 2 -------------------------
    # total = 0
    # for element in lst:
    #     total += sum_recursion_list(element) if isinstance(element,
    #                                                        list) else element
    # return total

    # ============================================================
    # ------------------------- METHOD 3 -------------------------
    total = 0
    for element in lst:
        if type(element) == type([]):
            total += sum_recursion_list(element)
        else:
            total += element
    return total

# ex:
# print(sum_recursion_list([1, 2, [3, 4], [5, 6]))  # 21


# ---------------------------------------------------------
# 4. Write a Python program to get the factorial of a non-negative integer using recursion.
def factorial(n: int) -> int:
    """Calculate the factorial of a given number using recursion.

    The factorial of a number n is the product of all positive integers from 1 to n.
    For example, factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.
    Note: factorial of 0 is defined to be 1.

    Args:
        n (int): A non-negative integer for which factorial needs to be calculated.

    Returns:
        int: The factorial of the input number.

    Raises:
        RecursionError: If input is too large leading to maximum recursion depth exceeded.
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# ex:
# print(factorial(5))  # 120

# ---------------------------------------------------------
# 5. Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n: int) -> int:
    """Calculate the nth number in the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.
    Args:
        n (int): The position in the Fibonacci sequence to calculate.
                Must be a positive integer greater than 0.
    Returns:
        int: The nth number in the Fibonacci sequence.
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than 1.
    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3) 
        2
        >>> fibonacci(7)
        13
    """
    if type(n) != int:  # not isinstance(n, int)
        raise TypeError("n must be an integer")
    elif n < 1:
        raise ValueError("n must be a positive integer greater than 0")

    return n * factorial(n - 1)


# ex:
# print(fibonacci(7))   # 13        => [0, 1, 1, 2, 3, 5, 8, 13]
# print(fibonacci(10))  # 55        => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# ---------------------------------------------------------
# 6. Write a Python program to get the sum of a non-negative integer using recursion.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9


def sum_digits(n: int) -> int:
    """Calculate the sum of digits of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer for which sum of digits needs to be calculated.

    Returns:
        int: The sum of digits of the input number.

    Raises:
        RecursionError: If input is too large leading to maximum recursion depth exceeded.
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Examples:
        >>> sum_digits(345)
        12
        >>> sum_digits(45)
        9
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
    # 345 % 10 + sum_digits(345 // 10)    ===   5 + sum_digits(34)
    # 34 % 10 + sum_digits(34 // 10)      ===   4 + sum_digits(3)
    # 3 % 10 + sum_digits(3 // 10)        ===   3 + sum_digits(0)
    # 5 + 4 + 3 = 12

# ex:
# print(sum_digits(345))  # 12


# ---------------------------------------------------------
# 7. Write a Python program to calculate the sum of the positive integers 
# of n+(n-2)+(n-4)... (until n-x= < 0) using recursion .
# In other words, we need to sum only even numbers of the series.
# Test Data:
# sum_series(6) -> 12   ===>>>  6 + 4 + 2 = 12
# sum_series(10) -> 30  ===>>>  10 + 8 + 6 + 4 + 2 = 30

def sum_series(n: int) -> int:
    """Calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x= < 0) using recursion.

    Args:
        n (int): A positive integer for which sum of series needs to be calculated.

    Returns:
        int: The sum of the series.

    Raises:
        RecursionError: If input is too large leading to maximum recursion depth exceeded.
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Examples:
        >>> sum_series(6)
        12
        >>> sum_series(10)
        30
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n <= 0:
        return 0
    return n + sum_series(n - 2)


# ex:
# print(sum_series(6))  # 12


# ---------------------------------------------------------

# 8. Write a Python program to calculate the sum of harmonic series upto n terms.
# In other words, we need to calculate the sum of 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n using recursion.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.

# harmonic_series(5) -> 2.283333333333333  ===>>> 1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283333333333333
#                                                 1 + 0.5 + 0.33 + 0.25 + 0.2 = 2.283333333333333

def harmonic_series(n: int) -> float:
    """Calculate the sum of harmonic series up to n terms.

    The harmonic series is defined as the sum: 1 + 1/2 + 1/3 + ... + 1/n

    Args:
        n (int): A positive integer indicating number of terms to sum

    Returns:
        float: The sum of the harmonic series up to n terms

    Raises:
        ValueError: If n is not a positive integer

    Examples:
        >>> harmonic_series(3)
        1.8333333333333333
        >>> harmonic_series(4)
        2.0833333333333335
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    return 1 / n + harmonic_series(n - 1)

# ex:
# print(harmonic_series(5))  # 2.283333333333333

# ---------------------------------------------------------
# 9. Write a Python program to calculate the geometric sum up to 'n' terms.
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
# In other words, a sequence of numbers where each term after the first is found by multiplying the 
# previous one by a fixed, non-zero number called the common ratio.
 
# geometric_sum(7)  ->  1.9921875   ===>>>  1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 = 1.9921875
# geometric_sum(4)  ->  1.9375      ===>>>  1 + 1/2 + 1/4 + 1/8 = 1.9375

def geometric_sum(n: int) -> float:
    """Calculate the geometric sum of a series 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^n).

    This function recursively computes the sum of a geometric series where each term
    is 1 divided by 2 raised to the power of the position (from 0 to n).

    Args:
        n (int): The number of terms in the series (must be non-negative)

    Returns:
        float: The sum of the geometric series up to the nth term

    Raises:
        ValueError: If n is negative

    Examples:
        >>> geometric_sum(0)
        1.0
        >>> geometric_sum(1)
        1.5
        >>> geometric_sum(2)
        1.75
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 1
    return 1 / (2 ** n) + geometric_sum(n - 1)

# ex:
# print(geometric_sum(7))  # 1.992187
# print(geometric_sum(4))  # 1.9375

# ---------------------------------------------------------
# 10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
# Test Data:
# power(3, 4) -> 81

def power(a: int, b: int) -> int:
    """
    Calculate the power of a number using recursion.

    Args:
        a (int): The base number.
        b (int): The exponent, must be a non-negative integer.

    Returns:
        int: The result of a raised to the power of b.

    Raises:
        ValueError: If b is a negative integer.

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    if b < 0:
        raise ValueError("b must be a non-negative integer")
    if b == 0:
        return 1
    return a * power(a, b - 1)


# ex:
# print(power(3, 4))  # 81


# ---------------------------------------------------------
# 11. Write a Python program to find the greatest common divisor 
# (GCD) of two integers using recursion.
# Test Data:
# gcd(12, 17) -> 1
# gcd(4, 6) -> 2
# gcd(336, 360) -> 24

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor (GCD) of two integers using recursion.

    The greatest common divisor (GCD) of two integers is the largest positive integer that divides
    each of the integers without a remainder.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Raises:
        ValueError: If either a or b is negative.

    Examples:
        >>> gcd(12, 17)
        1
        >>> gcd(4, 6)
        2
        >>> gcd(336, 360)
        24
    """
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative integers")
    if b == 0:
        return a
    return gcd(b, a % b)


# ex:
# print(gcd(12, 17))  # 1

