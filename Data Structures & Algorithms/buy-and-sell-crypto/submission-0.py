class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        profit = 0
        min_price = prices[0]
        for price in prices:
            profit = max(profit, price-min_price)
            min_price = min(min_price, price)
        
        return profit

"""
    10 1 5 6 7 1 20
10: 0  - - - - - 10
 1:  x 0 4 5 6 0 19 -> max

 6:        0 1 - 14



"""