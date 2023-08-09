# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# RU: есть лист, удалить n-й элемент с конца и вернуть его голову
def remove_nth_el(l: list, number: int):
    if len(l) == 0:
        return l
    elif number > len(l):
        return l

    return l[:number-1] + l[number:]


# ===================================================================================================
# ===================================================================================================
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
def find_smallest_int(nums: list):
    if len(nums) == 0:
        return 1

    for i in range(1, len(nums)+1):
        if i not in nums:
            return i


print(find_smallest_int([1, 2, 0]))  # 3
print(find_smallest_int([3, 4, -1, 1]))  # 2
print(find_smallest_int([7, 8, 9, 11, 12]))  # 1
# ===================================================================================================
# ===================================================================================================

x = "((x) (t (y) z)) (a) (b))"

# Given letters that are throughout paratneses ex: ((x), (t, (y), z)), (a), (b))
# Get the letters that are in/NOT in paratneses

# output
# letters in full paratneses: x, y, a, b
# letters not in full paratneses: t, z
# ===================================================================================================
# ===================================================================================================
