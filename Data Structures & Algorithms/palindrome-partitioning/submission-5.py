class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def isPali(l,r):
            # l ,r are the pointers in s that define the substring
            while l < r:
                if s[l] == s[r]:
                    l+= 1
                    r -= 1
                else:
                    return False
            return True
                        
        def back(left, path):
            if left == len(s):
                res.append(path.copy())
                return
            
            for right in range(left, len(s)):
                if isPali(left,right):
                    path.append(s[left:right+1])
                    back(right+1, path)
                    path.pop()
        
        back(0,[])
        return res



                

