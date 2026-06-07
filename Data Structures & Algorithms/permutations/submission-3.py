class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [False] * len(nums)
        res = []
        curr = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for idx in range(0,len(nums)):
                if visited[idx]:
                    continue
                
                visited[idx] = True
                curr.append(nums[idx])
                backtrack(curr)
                curr.pop()
                visited[idx] = False
        
        backtrack([])
        return res