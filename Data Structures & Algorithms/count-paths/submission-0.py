class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]* n for _ in range(m)]

        def dfs(down, right):

            if down == (m-1) and right == (n-1):
                return 1
            # bounds
            if down >= m or right >= n:
                return 0
            if memo[down][right] != -1:
                return memo[down][right]

            memo[down][right] =  dfs(down +1, right) + dfs(down, right + 1)
            return memo[down][right]
        
        return dfs(0,0)
