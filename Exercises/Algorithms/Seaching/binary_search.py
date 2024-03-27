# Iterative Binary Search


def binary_search(list, n):
    """This algorithm assumes the list is sorted"""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] < n:
            low = mid + 1
        elif list[mid] > n:
            high = mid - 1
        else:
            return mid

    return -1