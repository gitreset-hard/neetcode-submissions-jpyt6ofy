class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        used = [False] * len(nums)

        def dfs(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if used[j]:
                    continue
                
                used[j] = True
                curr.append(nums[j])
                dfs(j+1, curr)
                
                used[j] = False
                curr.pop()
        
        dfs(0,[])
        return res
