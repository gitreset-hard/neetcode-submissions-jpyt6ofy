class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        total = 0
        curr =[]
        def dfs(i, curXOR):
            nonlocal total

            if i >= len(nums):
                total += curXOR                    
                return
            # include curr in subset, then go to next
            dfs(i+1, curXOR ^ nums[i])
            dfs(i+1, curXOR)

        dfs(0,0)
        return total
            
            


