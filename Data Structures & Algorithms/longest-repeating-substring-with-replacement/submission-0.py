from collections import Counter, defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        no special characters or nums

        use map to track frequency and can only have 2 keys.
            one key freq <= k 

        window_len - keys <= 2
        """

        ans = 0
        left = 0
        seen = defaultdict(int)
        max_freq= 0
        for r in range(len(s)):
            
            seen[s[r]] = seen.get(s[r],0) + 1
            max_freq = max(max_freq, seen[s[r]])
            
            while ( r - left + 1 - max_freq) > k:
                seen[s[left]] -= 1
                left += 1
            
            ans = max(ans, r - left + 1)
        
        return ans