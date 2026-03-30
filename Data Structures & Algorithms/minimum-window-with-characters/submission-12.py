from collections import Counter, defaultdict
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ans_len = inf
        ans_start = 0
        want = Counter(t)
        required = len(want)
        have = defaultdict(int)


        left = 0
        for right in range(len(s)):
            char = s[right]

            have[char] += 1
            while all(want[c] <= have[c] for c in t):

                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_start = left
                
                have[s[left]] -= 1
                left += 1
        
        return s[ans_start: ans_start +ans_len] if ans_len!=inf else ""


            
