# Recursion

Recursion is a technique in programming where a function calls itself to solve a problem. It is a powerful tool for solving complex problems by breaking them down into smaller, more manageable subproblems. Recursion is widely used in computer science and is a fundamental concept in many algorithms and data structures.

## 📚 Key Concepts
1. Recursive function should always have an argument that changes with each call.
2. Recursive function should always check argument to determine when to stop.
3. In order to be able to call itself a recursive function, it should call itself with a different argument.


## 🚀 Example
```python
def factorial(n):
    """
    Function to calculate the factorial of a number using recursion
    Args:
        n: Integer number
    Returns:
        Factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example
print(factorial(5))  # Output: 120
```


## 📝 Resources
- [Recursion - Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Exercises on Recursion](../../w3resources/recursion.py)