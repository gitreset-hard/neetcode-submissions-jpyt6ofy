class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0
        memo = {}
        def dfs(i1, i2):
            if i2 == len(t):
                return 1 # found a match, processed all t
            if i1 >= len(s):
                return 0 
            
            if (i1,i2) in memo: return memo[(i1,i2)]

            # pick
            pick = 0
            if s[i1] == t[i2]:
                pick = dfs(i1+1, i2+1)
            # skip
            skip = dfs(i1+1, i2)
            memo[(i1,i2)] = pick + skip
            return memo[(i1,i2)]
        
        return dfs(0,0)