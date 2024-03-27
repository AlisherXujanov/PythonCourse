# Bubble search algorithm
# The bubble search algorithm is a simple algorithm that compares each element 
# in the list with the element next to it and swaps them if they are in the 
# wrong order. The pass through the list is repeated until no swaps are needed, 
# which means the list is sorted.

# The time complexity of the bubble search algorithm is O(n^2) in the worst case,
# where n is the number of elements in the list. This is because the algorithm
# makes multiple passes through the list, comparing each element with the next
# element. The space complexity of the bubble search algorithm is O(1), as it
# does not require any additional memory beyond a few variables to keep track
# of the elements being compared.

# The bubble search algorithm is not the most efficient sorting algorithm, as
# it has a worst-case time complexity of O(n^2). However, it is a simple algorithm
# to implement and understand, making it a good choice for small lists or for
# educational purposes.

def bubble_sort(uns_list:list[int]) -> list[int]:
    """
    This algorithm modifies the original list
    It uses a while loop
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(uns_list) - 1):
            if uns_list[i] > uns_list[i + 1]:
                uns_list[i], uns_list[i + 1] = uns_list[i + 1], uns_list[i]
                sorted = False

    return uns_list

l = [4, 1, 5, 6, 2, 3]
r = bubble_sort(l)
print(r)  # [1, 2, 3, 4, 5, 6]

# Original list = [4, 1, 5, 6, 2, 3]
# 1st step = [1, 4, 5, 6, 2, 3]
# 2nd step = [1, 4, 5, 2, 6, 3]
# 3rd step = [1, 4, 5, 2, 3, 6]
# 4th step = [1, 4, 2, 5, 3, 6]
# 5th step = [1, 4, 2, 3, 5, 6]
# 6th step = [1, 2, 4, 3, 5, 6]
# 7th step = [1, 2, 3, 4, 5, 6]
