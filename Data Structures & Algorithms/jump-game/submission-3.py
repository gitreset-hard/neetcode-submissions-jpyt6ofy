class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}        
        def dfs(idx):
            if idx in memo:
                return memo[idx]

            if idx == len(nums) - 1:
                return True
            
            if idx >= len(nums):
                return False

            for j in range(nums[idx], 0, -1):
                if dfs(idx + j):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False
        
        return dfs(0)
