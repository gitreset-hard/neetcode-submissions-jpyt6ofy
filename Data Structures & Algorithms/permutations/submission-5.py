class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = [False] * len(nums)

        def dfs (path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
        
            
            for i in range(len(nums)):

                if used[i] : continue

                path.append(nums[i])
                used[i] = True
                dfs(path)

                used[i] = False
                path.pop()
        
        dfs([])
        return res