class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        _max = 0
        streak = 0
        # 1 2 3 4
        for num in nums:
            # found a starting number
            if num - 1 not in nums_set:
                streak = 1
                while num + streak in nums_set:
                    streak += 1
                _max = max(_max, streak)
            
            
        return _max

