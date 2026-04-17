class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        self.start = 0
        self.max_len = 1

        def expand(l,r):
            while l >=0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1 > self.max_len:
                    self.max_len = r - l + 1
                    self.start = l
                
                l -= 1
                r += 1
            
        for i in range(len(s)):
            expand(i,i+1)
            expand(i,i)
        
        return s[self.start:self.start + self.max_len]

