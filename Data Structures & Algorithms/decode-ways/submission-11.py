class Solution:
    def numDecodings(self, s: str) -> int:
        
        valid = set((str(i) for i in range(1,27)))
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1

            if i in memo: return memo[i]

            if s[i] == '0': return 0

            ways = 0
            if i + 1 <= len(s) and s[i:i+1] in valid:
                ways += dfs(i+1)
            
            if i + 2 <= len(s) and  s[i:i+2] in valid:
                ways += dfs(i+2)
            
            memo[i] = ways
            return ways

        return dfs(0)
