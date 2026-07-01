class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = [-1] * len(nums)
        
        def dfs(idx):
            if idx >= len(nums):
                return 0 #?
            
            if memo[idx] != -1: return memo[idx]

            pick = dfs(idx+2) + nums[idx]
            skip = dfs(idx + 1)
            memo[idx] = max(pick, skip)
            return memo[idx]
        
        return dfs(0)



