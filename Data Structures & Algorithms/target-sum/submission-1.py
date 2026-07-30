class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0           

            
            add = dfs(i+1, total + nums[i])
            sub = dfs(i+1, total - nums[i])
            return add + sub
        
        return dfs(0, 0)