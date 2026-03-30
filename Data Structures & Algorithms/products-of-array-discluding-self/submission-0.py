
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # only 1 0?
        prod = 1 
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                prod *= num

        if count_zero > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if count_zero:
                res[i] = prod if num == 0 else 0
            else:
                res[i] = prod // num
        
        return res
