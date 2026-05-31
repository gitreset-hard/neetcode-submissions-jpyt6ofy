class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            requirements:
                - every substring partiotion must be a valid palindrome
            
            base case: single char is a valid palindrome
        """
        def isPali(l,r):
            while l < r:
                if s[l:r+1] in cache: return True
                
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            cache[s[l:r+1]] = True
            return True
        
        cache = {}
        res = []
        curr = []
        def backtrack(start):
            # only reach the end when all substrings in curr are valid
            if start == len(s):
                res.append(curr.copy())
                return

            # palindrome check starts at the first index
            # if yes, then dfs() starting at the next index, 
                # if at any point, not palindrome, stop and recurse
            for end in range(start, len(s)):
                if isPali(start,end):
                    curr.append(s[start:end+1])
                    backtrack(end+1)
                    curr.pop()
            
        backtrack(0)
        return res