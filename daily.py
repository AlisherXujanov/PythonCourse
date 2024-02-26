class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # METHOD 1
        max_profit = 0
        min_price = float('inf') # set to infinity
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
   
