class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # can't be split
        if total % 2 != 0:
            return False
        
        target = total // 2
        nums.sort()

        res = []
        curr = []
        memo = {}
        def backtrack(i, curr, total):
            # if one total can be found, then we know it works b/c the other can be true?
            # 4 6 5 5 -> [4,6] [5,5]
            # 7 4 3 8
            if total == target:
                return True
            
            if i >= len(nums) or total > target:
                return 

            if backtrack(i+1, curr + [nums[i]], total + nums[i]):
                return True
            
            if backtrack(i+1, curr, total):
                return True
            
            return False
        
        return backtrack(0,[],0)
        
        
        


        