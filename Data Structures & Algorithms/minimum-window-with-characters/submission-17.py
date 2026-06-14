from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):return ""

        window = defaultdict(int)
        want = Counter(t)
        formed = 0 # in the window
        ansLen = float('inf')
        ansStart = 0
        start = 0
        for end in range(len(s)):
            # add element
            window[s[end]] += 1
            # if the new element count matches our want, count it
            if window[s[end]] == want[s[end]]:
                formed += 1
            
            # when window is valid, try to shrink
            while formed == len(want.keys()):
                if end - start + 1 < ansLen:
                    ansLen = end - start + 1
                    ansStart = start
                    
                window[s[start]] -= 1
                if window[s[start]] == want[s[start]] -1:
                    formed -=1
                    
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1
        
        return "" if ansLen == float("inf") else s[ansStart:ansStart+ansLen]
