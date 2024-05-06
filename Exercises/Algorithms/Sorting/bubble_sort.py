def bubble_sort(numbers):
    ns_copy = numbers.copy()
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(ns_copy) - 1):
            if ns_copy[i] > ns_copy[i + 1]:
                ns_copy[i], ns_copy[i + 1] = ns_copy[i + 1], ns_copy[i]
                sorted = False

    print(ns_copy)
    return ns_copy

n = [5, 3, 8, 2, 1]
bubble_sort(n)
