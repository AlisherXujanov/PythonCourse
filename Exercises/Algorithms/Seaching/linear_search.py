# Linear Search Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

position = -1 # позиция (местоположение)
def search(list, n):
    i = 0 # i - индекс (или же счетчик)

    while i < len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i += 1
    return False

list = [5, 8, 4, 6, 9, 2]
n = 9

if search(list, n):
    print('Found at', position + 1)
else:
    print('Not Found')