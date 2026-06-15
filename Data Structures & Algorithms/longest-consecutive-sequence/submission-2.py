class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 0
        nums = set(nums)
        for num in nums:
            # start search at start of sequence
            if (num - 1) not in nums:
                # 2 3 4 5 6
                curr = 1
                start = num
                while start + 1 in nums:
                    curr += 1
                    start += 1

                count = max(count, curr)
        return count