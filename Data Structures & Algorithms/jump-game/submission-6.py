class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            
            
            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    return True
            return False
        
        return dfs(0)

