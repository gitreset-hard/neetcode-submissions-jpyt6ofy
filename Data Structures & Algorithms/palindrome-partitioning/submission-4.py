class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            - partition the whole string
            - backtracking?
        """
        res = []
        used = [False] * len(s) #??

        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        start = 0
        curr = []
        def backtrack(start):
            if start >= len(s):
                res.append(curr.copy())
                return
            
            for end in range(start, len(s)):
                if isPali(start,end):
                    curr.append(s[start:end+1])
                    backtrack(end+1)                    
                    curr.pop()
        
        backtrack(0)
        return res


        