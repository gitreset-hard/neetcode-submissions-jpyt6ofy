class Solution:
    def partition(self, s: str) -> List[List[str]]:
                
        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        res = []
        curr = []
        def backtrack(start):
            if start == len(s):
                res.append(curr.copy())
                return
            
            for end in range(start, len(s)):
                if isPali(start,end):
                    curr.append(s[start:end+1])
                    backtrack(end+1)
                    curr.pop()
            
        backtrack(0)
        return res