class Solution:
    def numDecodings(self, s: str) -> int:
        
        valid = set([str(i) for i in range(1,27)])

        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            if i in memo: return memo[i]

            ways = 0
            for idx in range(i, len(s)):
                if idx >= i + 2:
                    break
                if s[i:idx+1] in valid:
                    ways += dp(idx+1)
            
            memo[i] = ways

            return ways
            
        return dp(0)
                
                    

