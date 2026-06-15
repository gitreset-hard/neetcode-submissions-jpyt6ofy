class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k == 0:
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        used = [False] * len(nums)
        nums.sort(reverse=True)
        if nums[-1] > target: return False #?

        def back(idx, currSum, count):
            if count == k - 1:
                return True
            
            if currSum == target:
                return back(0,0,count + 1)
            

            for j in range(idx, len(nums)):
                if used[j] or currSum + nums[j] > target:
                    continue
                
                used[j] = True
                if back(j+1, currSum + nums[j], count):
                    return True
                used[j] = False

            return False
        
        return back(0,0,0)