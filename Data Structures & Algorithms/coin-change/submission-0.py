from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.ans = inf
        count = []

        def dfs(i, count, total):
            if total == amount:
                self.ans = min(self.ans, count)
                
            if total > amount: return

            if i >= len(coins): return

            if count > self.ans:
                return

            dfs(i, count + 1, total + coins[i])
            dfs(i+1, count, total)
        
        dfs(0,0,0)
        return -1 if self.ans == inf else self.ans
        



        

