from collections import Counter
from math import inf 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        want = Counter(t)
        required = len(want)

        have = defaultdict(int)
        formed = 0
        best_len = inf
        best_start = 0
        left = 0

        for r in range(len(s)):

            have[s[r]] += 1
            
            if s[r] in want and have[s[r]] == want[s[r]]:
                formed += 1

            while formed == required:

                if r - left + 1 < best_len:
                    best_len = r - left + 1
                    best_start = left
                
                have[s[left]] -= 1
                if s[left] in want and have[s[left]] < want[s[left]]:
                    formed -= 1
                left += 1


        
        return s[best_start:best_start+best_len] if best_len!= inf else ""
