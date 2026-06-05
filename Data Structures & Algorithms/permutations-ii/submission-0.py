class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        [1,1,2]
         x
         1,1,2 
         1,2,1
           x
           1,1,2
           1,2,1
             x
             2,1,1

        """
        nums.sort()
        res = []
        visited = [False] * len(nums)
        
        def dfs(curr):
            if len(curr) >= len(nums):
                res.append(curr.copy())
                return
            
            for idx in range(len(nums)):
                if visited[idx]:
                    continue
                
                if  idx > 0 and nums[idx] == nums[idx-1] and not visited[idx-1]:
                    continue
                
                curr.append(nums[idx])
                visited[idx] = True

                dfs(curr)

                curr.pop()
                visited[idx] = False
            
        dfs([])
        return res
