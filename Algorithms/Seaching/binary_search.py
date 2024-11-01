import random
numbers = list(range(100))     # список чисел от 0 до 99
target = random.randint(0, 199)  # цель (от 0 до 99)


def binary_search(l: list[int], target_number: int) -> bool:
    """Лист l должен быть отсортирован по возрастанию."""
    start = 0            # начало списка (начальный индекс)
    end = len(l) - 1     # конец списка  (конечный индекс)

    while start <= end:
        MID = (start + end) // 2
        if l[MID] == target_number:
            return True
        elif l[MID] < target_number:
            start = MID + 1
        else:
            end = MID - 1
    return False

if binary_search(numbers, target):
    print(f"Число {target} найдено!")
else:
    print(f"Число {target} не найдено!")
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================


def find_item(list, item):
    """
    The find_item function uses binary search to recursively locate an item in the list, 
    returning True if found, False otherwise.
    RU: Функция find_item использует двоичный поиск для рекурсивного нахождения элемента в списке, 
    возвращая True, если элемент найден, в противном случае - False.
    """
    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(list) // 2
    if list[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item in list[:middle]:
        return find_item(list[:middle], item)
    else:
        return find_item(list[middle + 1:], item)


# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan",
                 "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]


print(find_item(list_of_names, "Alex"))  # True
print(find_item(list_of_names, "Andrew"))  # False
print(find_item(list_of_names, "Drew"))  # True
print(find_item(list_of_names, "Jared"))  # False

# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
def binary_search(list, key):
    """
    The binary_search function returns the position of key in the list if found, or -1 if not found.
    RU: Функция binary_search возвращает позицию ключа в списке, если он найден, или -1, если не найден.
    """
    list.sort()  # Binary search starts with a sorted list
    left = 0  # The first value of the list
    right = len(list) - 1  # The last value of the list

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            print("Middle element")
            return middle
        elif list[middle] > key:
            print("Checking the left side")  # Add debug statement here
            right = middle - 1
        else:
            print("Checking the right side")  # Add debug statement here
            left = middle + 1
    return -1


print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================

# Напишите функцию, которая принимает упорядоченный список чисел 
# (список, в котором элементы сортированы от наименьшего к наибольшему) 
# и другое число. Функция решает, находится ли заданное число в списке, 
# и возвращает соответствующий булевый результат.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = random.randint(1, 10)

def binary_search(l: list, n: int) -> bool:
    middle = len(l) // 2

    tries = 0
    while n != l[middle]:
        tries += 1
        if l[middle] > n:
            l[:] = l[:middle]
        else:
            l[:] = l[middle+1:]

        middle = len(l) // 2

    print(f"За {tries} попыток нашли число {n} в списке {l}")
    return True

binary_search(l, number)
