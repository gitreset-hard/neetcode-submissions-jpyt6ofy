from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ 
        check: perm(s1) in s2
        permutation: total length stays same, order matters. ABC != CBA
            perm(s1): abc, acb, bca, bac,cab, cba
        
        # brute force:  O(n! * n)
            - create all perms O(N!) and then check if perm in s2 O(N)

        s1
            abc
        len    ^

        s2 
            "lecaabee"
        len.         ^             
        
        """
        
        if len(s1) > len(s2): return False

        left=0

        s1_freq = Counter(s1)
        window = Counter(s2[:len(s1)]) 

        if window == s1_freq: return True
        for right in range(len(s1), len(s2)):

            window[s2[right]] += 1
            left_char = s2[right - len(s1)]
            window[left_char] -= 1
            if window == s1_freq:
                return True
        
        return False




        
