class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i1, i2):

            if i1 == len(word1):
                return len(word2) - i2
            
            if i2 == len(word2):
                return len(word1) - i1
            if (i1,i2) in memo: return memo[(i1,i2)]
            
            if word1[i1] == word2[i2]:
                memo[(i1,i2)] = dfs(i1+1, i2+1 ) # no ops needed
                return memo[(i1,i2)]
                

            # insert: # only if not match?
            insert = 1 + dfs(i1, i2+1) # seems wrong
            # delete: skip char
            delete = 1 + dfs(i1+1, i2)
            # replace ( same as insert + delete)
            replace = 1 + dfs(i1+1, i2+1)
            memo[(i1,i2)] = min(insert, delete, replace)
            return memo[(i1,i2)] 
        
        return dfs(0,0)
