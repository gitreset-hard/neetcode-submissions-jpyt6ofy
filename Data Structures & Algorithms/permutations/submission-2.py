class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        1,2,3
        1,3,2
        2,1,3
        2,3,1
        3,1,2
        3,2,1
        """
        res = []
        visited = [False] * len(nums)
        curr = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for idx in range(len(nums)):
                if visited[idx]:
                    continue
                
                curr.append(nums[idx])
                visited[idx] = True
                dfs(curr)

                curr.pop()
                visited[idx] = False
        dfs([])
        return res
                