class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = 0
        maxSum = float('-inf')
        for num in nums:
            
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, num, currSum)
            
        
        return maxSum