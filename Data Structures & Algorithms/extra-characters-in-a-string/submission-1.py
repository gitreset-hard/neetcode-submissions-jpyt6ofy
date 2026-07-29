class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        res = float('inf')
        dictionary.sort(key = lambda x: len(x), reverse=True)
        memo = {len(s):0}

        def dfs(i):
            if i == len(s):
                return 0
            
            if i in memo: return memo[i]
            
            # skip curr char
            res = 1 + dfs(i+1) 

            # look for a match
            for word in dictionary:
                if s.startswith(word, i):
                    res = min(res, dfs(i + len(word)))
            memo[i] = res
            return res

        return dfs(0)





