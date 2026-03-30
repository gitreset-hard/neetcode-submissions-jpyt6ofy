from collections import Counter, defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ count sort """
        count = Counter(nums)

        idx = 0
        minVal, maxVal = min(nums), max(nums)
        for val in range(minVal, maxVal+1):
            # val: 0, 1, 2, 3, 4
            while count[val] > 0:
                nums[idx] = val
                idx += 1
                count[val] -= 1

        return nums
