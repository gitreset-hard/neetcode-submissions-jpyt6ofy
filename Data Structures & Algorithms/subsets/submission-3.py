class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            can only use a number once 

            recursive tree, at each option:
                - don't pick nums[i] (keep the array as is)
                - pick nums[i]
                - repeat with next num


        """
        res = []
        curr =[]
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res

