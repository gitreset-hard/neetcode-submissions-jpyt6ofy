from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        want = Counter(s1)
        if len(s1) > len(s2):
            return False
            
        for i in range(len(s1)):
            window[s2[i]] += 1
        
        if window == want:
            return True
        
        for end in range(len(s1),len(s2)):


            # remove from left
            start = end - len(s1)
            window[s2[start]] -= 1
            if window[s2[start]] == 0:
                del window[s2[start]]

            # add from right  
            window[s2[end]] += 1

            # discard invalid window
            if window == want:
                return True


        return False




