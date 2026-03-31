class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(idx, curPath, total):
            
            if total == target:
                res.append(curPath.copy())
                return

            if total > target or idx >= len(nums):
                return
            
            curPath.append(nums[idx])

            dfs(idx,curPath, total+nums[idx])
            curPath.pop()
            dfs(idx + 1, curPath, total)
        
        dfs(0,[],0)
        return res