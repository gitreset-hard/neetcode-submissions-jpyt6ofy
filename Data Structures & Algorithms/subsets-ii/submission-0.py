class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return [combo for combo in res]