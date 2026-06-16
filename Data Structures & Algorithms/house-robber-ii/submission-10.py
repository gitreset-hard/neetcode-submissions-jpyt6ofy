class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def robHouses(houses):

            memo = [-1] * len(houses)
            
            def dfs(i):
                if i >= len(houses):
                    return 0
                
                if memo[i] != -1: return memo[i]

                pick = houses[i] + dfs(i+2)
                skip = dfs(i+1)
                
                memo[i] = max(pick, skip)
                return memo[i]
                
            return dfs(0)
        
        return max(robHouses(nums[1:]), robHouses(nums[:-1]))