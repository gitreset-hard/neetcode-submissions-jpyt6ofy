class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        
            2 2 2 2 2 X
            2 2 2 2 X
            2 2 2 X
            2 2 5 √
            5 5 X
            5 6 X (maybe doesnt run bc 6 > 5) sorting could resolve this
            6 6 X
            9 √
        """

        self.output = []
        
        def dfs(idx, curPath, total):

            # bounds
            if idx >= len(nums) or total > target:
                return

            # validate and store answer
            if total == target:
                self.output.append(curPath.copy()) 
                return

            curPath.append(nums[idx])
            # recursion
                # same number can be chosen unlimited times
            dfs(idx, curPath, total + nums[idx])
            
            curPath.pop()
            
            # next indx
            dfs(idx + 1, curPath, total)
        
        dfs(0,[],0)
        return self.output

