
class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if memo[i] != -1: return memo[i]

            memo[i] = dfs(i + 1)
            if i < len(s) - 1:
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    memo[i] += dfs(i+2)

            return memo[i]
        
        return dfs(0)

