class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        unique = set(nums)
        for idx in range(len(nums)):
            if (nums[idx] - 1) not in unique:
                length = 1
                while nums[idx] + length in unique:
                    length += 1
                ans = max(ans, length)

        return ans
