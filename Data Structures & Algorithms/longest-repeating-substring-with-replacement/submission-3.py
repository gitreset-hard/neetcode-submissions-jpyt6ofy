from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = defaultdict(int)
        ans = 0
        max_freq = 0


        l = 0
        for r in range(len(s)):
            
            seen[s[r]] += 1
            max_freq = max(seen.values()) if seen else 0

            while r - l + 1 - max_freq > k:
                seen[s[l]] -= 1
                l += 1

            ans = max(ans, r-l +1)
        return ans