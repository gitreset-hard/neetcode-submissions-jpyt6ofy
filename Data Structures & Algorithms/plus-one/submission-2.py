class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            curr = digits[i] + carry
            carry = curr // 10
            digits[i] = curr % 10
            i -= 1
        
        if carry:
            return [carry] + digits
        else:
            return digits
