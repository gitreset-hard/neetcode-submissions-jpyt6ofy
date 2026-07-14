class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, path, rem, ):
            if rem == 0:
                res.append(path.copy())
                return
            
            if rem < 0 or i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(i, path, rem - nums[i])
            path.pop()

            dfs(i+1, path, rem)
        
        dfs(0,[], target)
        return res
