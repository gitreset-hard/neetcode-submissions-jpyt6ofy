class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        specials = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        
        total = 0
        i = 0
        
        while i < len(s):
            # Check if we can look ahead to form a pair
            if i + 1 < len(s) and s[i:i+2] in specials:
                total += specials[s[i:i+2]]
                i += 2  # Skip BOTH characters because we used the pair
            else: # normal char
                total += values[s[i]]
                i += 1  
                
        return total