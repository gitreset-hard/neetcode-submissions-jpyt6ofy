class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in memo: return memo[i]
            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)

