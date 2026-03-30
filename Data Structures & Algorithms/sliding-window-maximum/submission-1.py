from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            1 2 3 4 5
            l   r
            0   2     -> 2 - k + 1 = 2 - 3 + 1 = 0
        """
        output = []
        window = deque() # (idx)
        left = 0

        for idx, num in enumerate(nums):
            # ensure monotonic decreasing queue
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(idx)

            # remove from left if out of bound
            while window[0] < idx - k + 1:
                window.popleft()
            
            # when valid q
            if idx >= k - 1:
                output.append(nums[window[0]])
        
        return output