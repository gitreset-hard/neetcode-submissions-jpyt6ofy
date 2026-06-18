class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n:
            if n == 1:
                return True

            if n in seen:
                print(seen)
                return False

            total = 0
            curr = n
            seen.add(n)
            while curr:
                digit = curr % 10
                total += digit*digit
                curr = curr // 10
            
            n = total
        
        
        return True


            