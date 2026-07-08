class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        
        # str1 set to larger
        str1, str2 = max(str1,str2, key=len), min(str1,str2, key=len)


        # reducing 1 char from right every time
        # if it's truly repetive, this is fine else 
        for i in range(len(str2),0,-1):
            candidate = str2[:i]
            
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                multiplier = len(str1) // len(candidate)
                new_string = candidate * multiplier

                if new_string == str1:
                    return candidate
                
            
        return ""




            
            