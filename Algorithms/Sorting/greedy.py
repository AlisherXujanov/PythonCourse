# # A greedy algorithm is a simple, intuitive algorithm used in optimization problems, 
# which makes the locally optimal choice at each step with the hope that these local choices 
# will lead to a global optimum solution.

# # The algorithm makes the optimal choice at each step as it attempts to find the 
# overall optimal way to solve the entire problem. Greedy algorithms are quite successful 
# in some problems, such as Huffman encoding which is used in compression algorithms, 
# or Dijkstra's algorithm for finding the shortest path through a graph.

# # However, in many problems, a greedy strategy does not produce an optimal solution. 
# For example, in the problem of "Travelling Salesman", it does not provide a solution 
# in the general case.

# # In the context of the provided Python code, the greedy algorithm is used to find 
# the maximum profit that can be made by buying and selling a single share over a given 
# set of days. The algorithm keeps track of the minimum price and maximum profit seen so 
# far, making "locally optimal" decisions at each step (i.e., buying at the lowest price 
#                                                       seen so far and selling when the 
#                                                       profit is the highest).

class Solution(object):
    def maxProfit(self, prices):
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


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5

# min_price = 7,  max_profit = 0    <---  1 loop    ->  7
# min_price = 1,  max_profit = 0    <---  2 loop    ->  1
# min_price = 1,  max_profit = 4    <---  3 loop    ->  5   (greater than 0)
# min_price = 1,  max_profit = 4    <---  4 loop    ->  3   (not greater than 4)
# min_price = 1,  max_profit = 5    <---  5 loop    ->  6   (greater than 4)
# min_price = 1,  max_profit = 5    <---  6 loop    ->  4   (not greater than 5)
