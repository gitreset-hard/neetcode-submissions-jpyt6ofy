class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        picked = [False] * len(nums)
        
        def backtrack(perm):

            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    backtrack(perm)
                    perm.pop()
                    picked[i] = False
        
        backtrack([])
        return result
                
