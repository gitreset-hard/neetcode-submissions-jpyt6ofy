class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        def backtrack(idx, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if idx >= len(nums) or total > target:
                return
            

            # pick
            path.append(nums[idx])
            backtrack(idx, path, total + nums[idx])
            path.pop()
            # skip
            backtrack(idx+1, path, total)
        
        backtrack(0,[],0)
        return res