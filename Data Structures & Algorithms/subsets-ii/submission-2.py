class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def backtrack(start, curr):

            res.append(curr.copy())
            
            for end in range(start, len(nums)):
                if end > start and nums[end] == nums[end-1]:
                    continue
                    
                curr.append(nums[end])
                backtrack(end+1, curr)
                curr.pop()

        
        backtrack(0,curr)
        return res