from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i < len(s) - 1:
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    res += dfs(i+2)
            return res
        
        return dfs(0)

