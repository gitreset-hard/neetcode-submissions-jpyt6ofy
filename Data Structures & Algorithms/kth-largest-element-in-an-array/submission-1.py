import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        print(1, nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
