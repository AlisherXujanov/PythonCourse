# # Жадный (Greedy) алгоритм — это простой, интуитивно понятный алгоритм, используемый в задачах оптимизации,
# который делает локально оптимальный выбор на каждом шаге в надежде, что эти локальные выборы
# приведут к глобальному оптимальному решению.

# # Алгоритм делает оптимальный выбор на каждом шаге, пытаясь найти
# общий оптимальный способ решения всей задачи. Жадные алгоритмы весьма успешны
# в некоторых задачах (Но не всегда дают оптимальное решение для всех задач).

# # В контексте предоставленного кода, жадный алгоритм используется для нахождения
# максимальной прибыли, которую можно получить, купив и продав одну акцию за заданный
# набор дней. Алгоритм отслеживает минимальную цену и максимальную прибыль, наблюдаемые на данный момент, 
# принимая «локально оптимальные» решения на каждом шаге (т. е. покупая по самой низкой цене, наблюдаемой 
# на данный момент, и продавая, когда прибыль самая высокая).

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # ------------------------------------------
    # METHOD 1
    # SIMPLEST WAY

    # index = 1
    # max_profit = 0
    # for p in prices[:len(prices)-1]:
    #     diff = max(prices[index:]) - p
    #     diff = 0 if diff < 0 else diff
    #     if index < len(prices) and max_profit < diff:
    #         max_profit = diff
    #     index += 1
    # return max_profit
    # ------------------------------------------
    # ------------------------------------------
    # METHOD 2
    # GREEDY ALGORITHM (TIME COMPLEXITY O(n))

    max_profit = 0
    min_price = float('inf')  # set to infinity
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5

# min_price = 7,  max_profit = 0    <---  1 loop    ->  7
# min_price = 1,  max_profit = 0    <---  2 loop    ->  1
# min_price = 1,  max_profit = 4    <---  3 loop    ->  5   (greater than 0)
# min_price = 1,  max_profit = 4    <---  4 loop    ->  3   (not greater than 4)
# min_price = 1,  max_profit = 5    <---  5 loop    ->  6   (greater than 4)
# min_price = 1,  max_profit = 5    <---  6 loop    ->  4   (not greater than 5)
