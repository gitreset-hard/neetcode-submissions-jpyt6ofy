class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = min(text1, text2), max(text1, text2)
        memo = {}
        
        res = 0
        def dfs(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2) :
                return 0 # no more possible?
            
            key = (i1, i2)
            if key in memo: return memo[key]
            # matches 
            if text1[i1] == text2[i2]:
                match = 1 + dfs(i1+1, i2+1)
                memo[key] = match
                return memo[key]
            # else try 1 or other
            else:
                skip1 = dfs(i1 + 1, i2) 
                skip2 = dfs(i1, i2 + 1)
                memo[key] = max(skip1, skip2)
                return memo[key]
        
        return dfs(0,0)

            