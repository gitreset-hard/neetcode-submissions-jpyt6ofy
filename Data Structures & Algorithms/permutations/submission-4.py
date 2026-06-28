class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * len(nums)

        res = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            
            for end in range(len(nums)):
                if visited[end]:
                    continue
                
                curr.append(nums[end])
                visited[end] = True
                backtrack(curr)

                curr.pop()            
                visited[end] = False
        
        backtrack([])
        return res
