class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(steps, memo = {}):
            if steps in memo: return memo[steps]
            if steps < 0:
                return 0
            if steps in (0,1):
                return 1
            if steps == 2:
                return 2
            memo[steps] = dfs(steps - 1, memo) + dfs(steps - 2, memo)
            return memo[steps]
        
        return dfs(n)
