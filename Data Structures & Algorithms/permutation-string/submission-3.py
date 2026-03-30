from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
            lowercase or upper?
            need s1 freq in s2

        """
        if len(s1) > len(s2): return False

        want = Counter(s1)
        have = defaultdict(int) # {a: 0, b:0}
        
        for char in s2[:len(s1)]:
            have[char] += 1
        
        if have == want: return True
        left = 0
        for r in range(len(s1), len(s2)):
            have[s2[r]] += 1
            
            have[s2[left]] -= 1
            if have[s2[left]] == 0: del have[s2[left]]
            left += 1
            
            if have == want:
                return True

        return False

            
