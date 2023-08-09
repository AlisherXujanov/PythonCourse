# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# RU: # Дана голова зв'язаного списку, видаліть n-й вузол з кінця списку і поверніть його голову
def remove_nth_el(l: list, number: int):
    if len(l) == 0:
        return l
    elif number > len(l):
        return l

    return l[:number-1] + l[number:]


# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# RU: # Для даного невідсортованого масиву цілих чисел поверніть найменше відсутнє додатнє ціле число.
# Ви повинні реалізувати алгоритм, який працює за час O (n) і використовує допоміжний простір O (1).
def find_smallest_int(nums: list):
    if len(nums) == 0:
        return 1

    nums.sort()
    for i in range(1, len(nums)+1):
        if i not in nums:
            return i


print(find_smallest_int([1, 2, 0]))  # 3
print(find_smallest_int([3, 4, -1, 1]))  # 2
print(find_smallest_int([7, 8, 9, 11, 12]))  # 1
