class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def robHouses(houses):

            memo = [-1] * len(houses) 
            def rob(idx):
                if idx >= len(houses):
                    return 0
                
                if memo[idx] != -1:
                    return memo[idx]

                pick = houses[idx] + rob(idx+2)
                skip = rob(idx+1)
                memo[idx] = max(pick, skip)
                return memo[idx]
            
            return rob(0)
        
        return max(robHouses(nums[1:]), robHouses(nums[:-1]))
            