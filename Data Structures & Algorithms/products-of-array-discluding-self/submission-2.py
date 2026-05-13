class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        for idx in range(1,len(nums)):
            left[idx] = left[idx-1] * nums[idx-1]
        
        right = [1] * len(nums)
        for idx in range(len(nums)-2,-1,-1):
            right[idx] = right[idx+1] * nums[idx+1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res