class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        memo = {}

        def calc(i, state):
            if i >= len(prices): return 0

            if (i,state) in memo: return memo[(i,state)]
            # buy
            if state == 1: 
                buy = -prices[i] + calc(i+1, -1)
                skip = calc(i+1, 1)
                memo[(i,state)] = max(buy, skip)
                return memo[(i,state)]
            
            # sell
            elif state == -1: 
                sell = prices[i] + calc(i+2, 1) # buy again after cooldown
                skip = calc(i+1, -1) # stil need to sell
                memo[(i,state)] = max(sell, skip)
                return memo[(i, state)]
            
        return calc(0, 1)
        
        