class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = 2**31      - 1
        is_neg = x < 0
        new_num = 0
        x = abs(x)

        while x:
            pop = x%10
            x //= 10

            if new_num > (LIMIT-pop)//10:
                return 0
            
            new_num = new_num * 10 + pop
            

        return -new_num if is_neg else new_num
        