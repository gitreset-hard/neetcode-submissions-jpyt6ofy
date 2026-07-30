class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}

        def dp(i, total):
            if i >= len(coins) or total > amount:
                return 0
            
            if total == amount:
                return 1
            
            key = (i, total)
            if key in memo: return memo[key]

            pick = dp(i, total + coins[i])
            skip = dp(i+1, total)

            memo[key] =  pick + skip
            return memo[key]
        return dp(0,0)


            
            
