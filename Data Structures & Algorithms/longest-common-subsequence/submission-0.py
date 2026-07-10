class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ans = 0
        memo = {}
        def dfs(idx1, idx2):
            nonlocal ans
            # no more possible matches?
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0 #?
            
            if (idx1,idx2) in memo: return memo[(idx1, idx2)]

            if text1[idx1] == text2[idx2]:
                pick = 1 + dfs(idx1 + 1, idx2 + 1)
                memo[(idx1, idx2)] = pick
                return pick
            else:
                skip1 = dfs(idx1, idx2 + 1)
                skip2 = dfs(idx1 + 1, idx2)
                memo[(idx1, idx2)] =  max(skip1, skip2)
                return max(skip1, skip2)



        return dfs(0,0)

                
            
