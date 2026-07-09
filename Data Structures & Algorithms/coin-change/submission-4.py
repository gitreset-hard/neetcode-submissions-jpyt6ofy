class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoins = float('inf')
        memo = {}
        def dfs(rem, used):
            nonlocal minCoins

            if (rem,used) in memo: return memo[(rem,used)]
            if rem < 0:
                return float('inf')
            
            if used > minCoins: return
            memo[(rem,used)] = minCoins
            if rem == 0:
                minCoins = min(used, minCoins)    
                return 
            
            for coin in coins:
                if rem - coin >= 0:
                    dfs(rem-coin, used + 1)
            
        dfs(amount, 0)
        return -1 if minCoins == float('inf') else minCoins



        
