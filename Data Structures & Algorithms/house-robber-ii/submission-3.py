class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_houses(houses):
            memo  = [-1] * len(nums)

            def dfs(i):
                if i >= len(houses):
                    return 0

                if memo[i] != -1: return memo[i]

                skip = dfs(i+1)
                pick = dfs(i + 2) + houses[i]
                memo[i] = max(skip, pick)
            
                return memo[i]
            return dfs(0)
        

            
        return max(rob_houses(nums[1:]), rob_houses(nums[:-1]))
        