from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            A:3
            B:1  -> k-1 = 0
            most_freq + others = r - l + 1 = len
            invalid if
                len - most_freq > k

        """
        
        ans = 0
        window = defaultdict(int)
        most_freq = 0
        start = 0
        for end in range(len(s)):

            window[s[end]] += 1
            most_freq = max(most_freq, window[s[end]])

            # valid window check, make valid
            while end - start + 1 - most_freq > k:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1
            
            ans = max(ans, end - start + 1)
        
        return ans