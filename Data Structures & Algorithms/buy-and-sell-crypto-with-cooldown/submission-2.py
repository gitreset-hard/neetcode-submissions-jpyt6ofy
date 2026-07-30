class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # state
        # -1: have to sell
        # 0: hold #?
        # 1: have to buy
        memo = {}

        def dfs(i, state):
            if i >= len(prices): 
                return 0 # not possible to sell anymore

            key = (i, state)
            if key in memo: return memo[key]

            if state == 1:
                buy = -prices[i] + dfs(i+1, -1)
                wait = dfs(i+1, 1)
                memo[key] =  max(buy, wait)
                return memo[key]
            elif state == -1:
                sell = prices[i] + dfs(i+2, 1)
                hold = dfs(i+1, -1)
                memo[key] = max(sell, hold)
                return memo[key]
        
        return dfs(0,1)



