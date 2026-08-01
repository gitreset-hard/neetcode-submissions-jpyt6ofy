class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [0] * len(s)
        zeros[0] = 1 if s[0] == "0" else 0

        ones = [0] * len(s)
        ones[-1] = 1 if s[-1] == "1" else 0

        for i in range(1, len(s)):
            zeros[i] = zeros[i-1] + (1 if s[i] == "0" else 0)

        for i in range(len(s)-1-1, -1,-1):
            ones[i] = ones[i+1] + (1 if s[i] == "1" else 0)
        
        print(ones)
        print(zeros)
        res = 0
        for i in range(1,len(s)):
            res = max(res, zeros[i-1] +  ones[i])        
        return res