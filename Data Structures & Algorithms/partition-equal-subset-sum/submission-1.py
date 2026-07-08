class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # can't be split
        if total % 2 != 0:
            return False
        
        target = total // 2
        nums.sort()

        res = []
        used = [False] * len(nums)
        memo = {}
        def backtrack(i, total):
            # if one total can be found, then we know it works b/c the other can be true?
            # 4 6 5 5 -> [4,6] [5,5]
            # 7 4 3 8
            if total == target:
                return True
            
            if i >= len(nums) or total > target:
                return False

            for idx in range(len(nums)):
                if used[idx]  or nums[idx] + total > target:
                    continue
                
                used[idx]  = True
                if backtrack(idx+1, total + nums[idx]):
                    return True
                used[idx] = False

            return False
        
        return backtrack(0,0)
        
        
        


        