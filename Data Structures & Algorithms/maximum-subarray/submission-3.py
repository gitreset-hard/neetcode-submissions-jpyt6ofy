class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        currSum = 0

        for num in nums:
            currSum = max(num, currSum + num)
            res = max(res, currSum)
        return res
