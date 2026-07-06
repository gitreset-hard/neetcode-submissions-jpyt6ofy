class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for idx in range(len(nums)):
                if used[idx]:
                    continue
                
                if idx > 0 and nums[idx] == nums[idx-1] and not used[idx-1]:
                    continue

                used[idx] = True
                path.append(nums[idx])
                backtrack(path)
                
                path.pop()
                used[idx] = False
        
        backtrack([])
        return res

