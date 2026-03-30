from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        want = Counter(s1)
        right = 0
        
        n1 = len(s1)
        n2 = len(s2)
        have = Counter(s2[:n1])
        if have == want:
            return True
        
        left = len(s1)
        for right in range(n1,n2):
            have[s2[right]] = have.get(s2[right],0) + 1
            have[s2[right-n1]] -= 1
            
            if have == want:
                return True
        return False
            
