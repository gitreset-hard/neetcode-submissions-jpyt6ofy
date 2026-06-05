class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
    
        def dfs(i,curr, curr_total):

            if curr_total == target:
                res.append(curr.copy())
                return
            
            # out of bounds
            if i >= len(nums) or curr_total > target:
                return

            dfs(i, curr + [nums[i]], curr_total + nums[i])

            dfs(i + 1, curr, curr_total )
            return 
        
        dfs(0,curr,0)
        return res