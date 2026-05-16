from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        window = defaultdict(int)
        want = Counter(s1)
        
        for right in range(len(s1)):
            window[s2[right]] += 1
        
        if want == window:
            return True
        
        for right in range(len(s1), len(s2)):
            
            window[s2[right - len(s1)]] -= 1
            if window[s2[right - len(s1)]] == 0:
                del window[s2[right - len(s1)]]
            
            window[s2[right]] += 1
            if window == want:
                return True
        
        return False

