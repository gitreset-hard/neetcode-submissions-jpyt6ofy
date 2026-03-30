from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        ans = 0
        right = 0
        count = defaultdict(int)
        n = len(s)
        max_f = 0
        left = 0
        for right in range(n):

            count[s[right]] += 1
            max_f = max(count.values()) if count else 0
            # failure condition
            while right - left + 1 - max_f > k:
                count[s[left]] -= 1
                left += 1
                max_f = max(count.values()) if count else 0
            
            ans = max(ans, right - left + 1)
                      
            
        
        return ans