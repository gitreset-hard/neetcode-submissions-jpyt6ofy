class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for idx in range(len(digits)-1,-1,-1):
            if digits[idx] == 9:
                digits[idx] = 0
                carry = 1
                continue

            else:
                digits[idx] += 1
                return digits
        
        return [1] + digits
                