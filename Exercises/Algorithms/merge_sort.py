# MERGE SORT
# Merge sort is a divide and conquer algorithm - Алгоритм сортировки слиянием

# It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves
# RU: Алгоритм сортировки слиянием делит входной массив на две половины, вызывает 
# себя для двух половин и затем сливает две отсортированные половины

# The merge() function is used for merging two halves
# RU: Функция merge() используется для слияния двух половин

# Advantage of Merge Sort - Приемущество сортировки слиянием
# - stable - стабильный
# - comparison-based - сравнительный
# - recursive - рекурсивный

# Disadvantage of Merge Sort - Недостаток сортировки слиянием
# - has a space complexity of O(n) which means it uses a lot of memory
# RU: занимает много памяти из-за создания дополнительных списков
# - has a time complexity of O(n log n) which means it is not the fastest algorithm
# RU: не самый быстрый алгоритм сортировки из-за большого количества операций сравнения и перемещения элементов


nums = [2, 6, 5, 1, 7, 3, 4, 8, 9]


def merge_sort(nums):
    """
        This algorithm does not modify the original list
        It uses recursion
    """
    if len(nums) > 1:
        MID = len(nums) // 2
        left_half = nums[:MID]
        right_half = nums[MID:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Iterators for the list
        i = 0
        j = 0
        k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Check if there are any elements left
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

    return nums


print(merge_sort(nums))