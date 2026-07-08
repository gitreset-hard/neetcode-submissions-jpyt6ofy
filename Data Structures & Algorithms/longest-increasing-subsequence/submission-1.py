class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        n = len(nums)
        dp = [1] * n

        for right in range(n):

            for start in range(right):
                if nums[right] > nums[start]:

                    dp[right] = max(dp[right], dp[start] + 1)
        
        return max(dp)