class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        visited = [False] * len(nums)

        def dfs(curPath):
            if len(curPath) == len(nums):
                res.append(curPath.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                curPath.append(nums[i])
                visited[i] = True
                dfs(curPath)

                curPath.pop()
                visited[i] = False
        
        dfs([])
        return res