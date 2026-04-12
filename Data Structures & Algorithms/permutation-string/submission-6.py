from collections import Counter , defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        want = Counter(s1)
        have = defaultdict(int)

        for i in range(len(s1)):
            have[s2[i]] += 1
        
        if have == want: return True

        for i in range(len(s1), len(s2)):

            have[s2[i]] += 1
            have[s2[i-len(s1)]] -= 1
            if have[s2[i-len(s1)]] == 0:
                del have[s2[i-len(s1)]]
            
            if have == want:
                return True
        
        return False
        
        