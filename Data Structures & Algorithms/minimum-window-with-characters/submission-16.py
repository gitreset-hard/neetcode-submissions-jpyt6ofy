from collections import Counter, defaultdict
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        ans_len = inf
        ans_start = 0

        want = Counter(t)
        have = defaultdict(int)
        formed = 0
        left = 0

        for right in range(len(s)):

            have[s[right]] += 1
            if have[s[right]] == want[s[right]]:
                formed += 1
            
            while formed == len(want.keys()):
                
                if (right - left + 1) < ans_len:
                    ans_len = right - left + 1
                    ans_start = left
                
                have[s[left]] -= 1
                if have[s[left]] == want[s[left]] - 1:
                    formed -= 1
                left += 1

        return '' if ans_len == inf else s[ans_start:ans_len + ans_start]