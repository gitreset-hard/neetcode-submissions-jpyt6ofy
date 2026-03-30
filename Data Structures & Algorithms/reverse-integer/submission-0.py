class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31
        MIN = -1*MAX
        num = 0
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        while x:
            num = num*10 + x%10
            x = x//10

        num*= sign

        if MIN < num < MAX:
            return num
        else:
            return 0