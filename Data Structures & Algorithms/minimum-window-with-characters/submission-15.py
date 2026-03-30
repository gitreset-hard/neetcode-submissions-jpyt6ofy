from collections import Counter, defaultdict
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ans_start = 0
        ans_len = inf
        right = 0
        have = defaultdict(int)
        want = Counter(t)
        left = 0
        for right in range(len(s)):
            have[s[right]] += 1
            while all(have[c] >= want[c] for c in t):
                if right - left + 1 < ans_len:
                    ans_start = left
                    ans_len = right - left + 1
                have[s[left]] -= 1
                left += 1

        
        return s[ans_start:ans_start+ans_len] if ans_len < inf else ""
            
            